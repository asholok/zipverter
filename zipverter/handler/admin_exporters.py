from import_export import resources
from cities.models import City , Region, Country, District


class CityAdmin(resources.ModelResource):
    class Meta:
        model = City
        fields = ('name' ,'name_std', 'country__name', 'population', 'region__name_std', 'timezone')
    

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

