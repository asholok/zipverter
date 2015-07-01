from tastypie import resources
from handler.models import LocationTable
from handler.lazy_load import find_city
from tastypie.authorization import Authorization
import json
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
    
    def obj_create(self, bundle, request=None, **kwargs):
        country = bundle.data['country']
        zip_code = bundle.data['zip_code']

        try:
            location_obj = LocationTable.objects.get(country=country, zip_code=zip_code)
            city = location_obj.city     
            raise ImmediateHttpResponse(response=HttpResponse(content=json.dumps({'city': city}),status='200'))
        except LocationTable.DoesNotExist:
            city = find_city(zip_code, country)
            if city:
                bundle.data['city'] = city
                return super(ZipTableResource, self).obj_create(bundle, request=request, **kwargs)
            error = 'Country and zip code missmatch'
            raise ImmediateHttpResponse(response=HttpResponse(content=json.dumps({'error': error}),status='200'))

