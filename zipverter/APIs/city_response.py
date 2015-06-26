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
        zip_code = bundle.data['zip']
        country = bundle.data['country']
        city = find_city(zip_code, country)

        if city:
            obj = LocationTable(country=country, zip_code=zip_code, city=city)
            obj.save()

        else:
            pass


    def dehydrate(self, bundle):
        zip_code = bundle.data['zip']
        country = bundle.data['country']
        filtered = LocationTable.objects.filter(country=country, zip_code=zip_code)
        
        if filtered:
            Meta.queryset = filtered
        else:
            self.obj_create(bundle)


