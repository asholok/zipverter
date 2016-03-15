import json
import re
from tastypie import resources
from handler.models import LocationTable, LoggForLocationTable
from handler.lazy_load import find_location_info
from tastypie.authorization import Authorization
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse

SUBINFOCOUNTRIES = ['United States', 'Brazil']
WHITE_LIST = ['United Kingdom', 'Canada', 'New Zealand', 'Australia', 'South Africa']


def shortfy_country_name(country):
    if country in WHITE_LIST:
        if country == 'South Africa':
            return "-South-Africa"
        words = country.split(' ')
        if len(words) > 1:
           return "-" + ''.join([word[0] for word in words])
        return "-" + country
    return ''

class ZipTableResource(resources.ModelResource):

    class Meta:
        queryset = LocationTable.objects.all()
        resource_name = 'zip_table'
        fields = [
            'city', 
            'zip_code', 
            'country', 
            'state', 
            'state_code', 
            'district',
            'timezone'
        ]
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()
    
    def __create_logg(self, request, response, meta):
        client_ip = meta.get('HTTP_X_FORWARDED_FOR')
        """ For use on localhost """
        
        if not client_ip:
            client_ip = '127.0.0.1'
        logg = LoggForLocationTable(
            request=request,
            response=response,
            client_ip=client_ip
        )
        logg.save()

    def __create_response(self, zip_code, country):
        location_obj = LocationTable.objects.get(country=country, zip_code=zip_code)
        city_name = city_alias = location_obj.city
        city_alias = re.sub(r'[().,*\'"]', '', city_alias)
        city_alias = city_alias.replace(" ", "-")
        
        if country in SUBINFOCOUNTRIES:
            if location_obj.state_code == '': # Only for prod database to fullfill state_code for existing LocationTable
                location_obj.state_code = find_location_info(zip_code, country)['state_code']
                location_obj.save()
            state_code = location_obj.state_code
            state = location_obj.state
            if state_code not in city_alias:
                city_alias += "-" + state_code
            if state not in city_name:
                city_name += ', ' + state_code
            return {
                        # 'city': location_obj.city, 
                        'city_name': city_name, 
                        'city_alias': city_alias + shortfy_country_name(country), 
                        # 'state': state, 
                        # 'state_code': state_code, 
                        'district': location_obj.district,
                        'timezone': location_obj.timezone
                    }
        return {
                    'city_name': city_name, 
                    'city_alias': city_alias + shortfy_country_name(country), 
                    'timezone': location_obj.timezone 
                }

    def __prepare_special_zip(self, country, zip_code):
        zip_code = zip_code.split(' ')[0]
        if country == 'Canada' and len(zip_code) > 3:
            zip_code = zip_code[:3]
        if country == 'Brazil':
            zip_code = re.sub(r'[-]', '', zip_code)
        return zip_code.upper()


    def obj_create(self, bundle, request=None, **kwargs):
        country = bundle.data['country']
        zip_code = self.__prepare_special_zip(country, bundle.data['zip_code'])
        try:
            response = self.__create_response(zip_code, country)
            self.__create_logg(bundle.data, response, bundle.request.META)
            raise ImmediateHttpResponse(response=HttpResponse(
                                            content=json.dumps(response),
                                            status=200
                                        ))
        except LocationTable.DoesNotExist:
            location_info = find_location_info(zip_code, country)
            error_response = {'error':'Country and zip code missmatch'}
            if location_info:
                bundle.data['city'] = location_info['city']
                bundle.data['zip_code'] = zip_code
                bundle.data['state'] = location_info['state'] 
                bundle.data['state_code'] = location_info['state_code']
                bundle.data['timezone'] = location_info.get('timezone', '')
                bundle.data['district'] = location_info.get('district', '')
                super(ZipTableResource, self).obj_create(bundle, request=request, **kwargs)
                return self.obj_create(bundle, request=request, **kwargs)
            
            self.__create_logg(bundle.data, error_response, bundle.request.META)
            raise ImmediateHttpResponse(response=HttpResponse(
                                            content=json.dumps(error_response),
                                            status=200
                                        ))

