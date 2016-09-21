from import_export import resources, fields
from cities.models import City , Region, Country, District


class CityAdmin(resources.ModelResource):
    ru_name = fields.Field()

    class Meta:
        model = City
        fields = ('name' ,'name_std', 'country__name', 'population', 'ru_name','region__name_std', 'timezone')
    
    def dehydrate_ru_name(self, obj):
        try:
            return obj.alt_names.get(language='ru').name
        except:
            return 'N/A'


class RegionAdmin(resources.ModelResource):
    class Meta:
        model = Region
        fields = ('name_std', 'country__name')


class CountryAdmin(resources.ModelResource):
    class Meta:
        model = Country
        fields = ('name', 'population')


class DistrictAdmin(resources.ModelResource):
    class Meta:
        model = Country
        fields = ('name_std', 'city__name_std')

