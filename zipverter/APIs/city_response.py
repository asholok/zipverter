import json
from tastypie import resources
from handler.models import LocationTable, LoggForLocationTable
from handler.lazy_load import find_city, find_state
from tastypie.authorization import Authorization
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse

class ZipTableResource(resources.ModelResource):

    class Meta:
        queryset = LocationTable.objects.all()
        resource_name = 'zip_table'
        fields = ['city', 'zip_code', 'country', 'state']
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

        if country == 'United States':
            return {'city': location_obj.city, 'state': location_obj.state}
        return {'city': location_obj.city}

    def __prepare_special_zip(self, zip_code):
        zip_code = zip_code.split(' ')[0]

        return zip_code.upper()


    def obj_create(self, bundle, request=None, **kwargs):
        country = bundle.data['country']
        zip_code = self.__prepare_special_zip(bundle.data['zip_code'])

        try:
            response = self.__create_response(zip_code, country)
            self.__create_logg(bundle.data, response, bundle.request.META)
            raise ImmediateHttpResponse(response=HttpResponse(
                                            content=json.dumps(response),
                                            status=200
                                        ))
        except LocationTable.DoesNotExist:
            city = find_city(zip_code, country)
            error_response = {'error':'Country and zip code missmatch'}
            
            if city:
                bundle.data['city'] = city
                bundle.data['zip_code'] = zip_code
                bundle.data['state'] = find_state(zip_code, country)
                super(ZipTableResource, self).obj_create(bundle, request=request, **kwargs)
                return self.obj_create(bundle, request=request, **kwargs)
            
            self.__create_logg(bundle.data, error_response, bundle.request.META)
            raise ImmediateHttpResponse(response=HttpResponse(
                                            content=json.dumps(error_response),
                                            status=200
                                        ))

