import json
from tastypie import resources
from handler.models import LocationTable, LoggForLocationTable
from handler.lazy_load import find_city
from tastypie.authorization import Authorization
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse

class ZipTableResource(resources.ModelResource):

    class Meta:
        queryset = LocationTable.objects.all()
        resource_name = 'zip_table'
        fields = ['city', 'zip_code', 'country']
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()
    
    def __create_logg(self, request, response, meta):
        client_ip = meta.get('HTTP_X_FORWARDED_FOR')
        logg = LoggForLocationTable(
            request=request,
            response=response,
            client_ip=client_ip
        )

        logg.save()

    def obj_create(self, bundle, request=None, **kwargs):
        country = bundle.data['country']
        zip_code = bundle.data['zip_code']

        print "-------------------------------------------------------------"
        print bundle.data
        print bundle.request.META
        print "-------------------------------------------------------------"

        try:
            location_obj = LocationTable.objects.get(country=country, zip_code=zip_code)
            response = {'city': location_obj.city}
            
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
                return super(ZipTableResource, self).obj_create(bundle, request=request, **kwargs)
            self.__create_logg(bundle.data, error_response, bundle.request.META)
            raise ImmediateHttpResponse(response=HttpResponse(
                                            content=json.dumps(error_response),
                                            status=200
                                        ))

