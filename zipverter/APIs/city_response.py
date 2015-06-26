from tastypie import resources
from handler.models import LocationTable
from handler.lazy_load import find_city

class ZipTableResource(resources.ModelResource):

    class Meta:
        queryset = LocationTable.objects.all()
        resource_name = 'zip_table'
        fields = ['city']
        allowed_methods = ['get', 'post']
        always_return_data = True

    def obj_create(self, bundle, request=None, **kwargs):
        response = {}
        zip_code = bundle.data['zip']
        country = bundle.data['country']
        filtered = LocationTable.objects.filter(country=country, zip_code=zip_code)
        
        if filtered:
            response['city'] = filtered[0]
        else:    
            city = find_city(zip_code, country)
            
            if city:
                obj = LocationTable(country=country, zip_code=zip_code, city=city)
                obj.save()
                response['city'] = city
            else: 
                response['errore'] = 'Country and zip code missmatch'

        return self.create_response(request, response, None, **kwargs)



