from django.contrib import admin
from import_export.admin import ExportMixin
from cities.models import City, Region, Country, District
from handler.admin_exporters import CityAdmin, RegionAdmin, CountryAdmin, DistrictAdmin


class CityAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name', 'name_std', 'country', 'ru_name', 'population', 'region', 'timezone']
    exclude = ('alt_names',)
    search_fields = ('country__name', 'name_std')
    list_filter = ['country']
    raw_id_fields = ['country', 'region']
    resource_class = CityAdmin

    def ru_name(self, obj):
        try:
            return obj.alt_names.get(language='ru').name
        except:
            return 'N/A'


class RegionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name', 'name_std', 'code', 'country']
    search_fields = ('country__name',)
    raw_id_fields = ['country']
    resource_class = RegionAdmin


class CountryAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name', 'population', 'languages', 'capital', 'currency_name', 'currency']
    search_fields = ('continent',)
    resource_class = CountryAdmin


class DistrictAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name', 'name_std', 'population', 'city']
    search_fields = ('city__name',)
    raw_id_fields = ['city']
    resource_class = DistrictAdmin


admin.site.unregister(City)
admin.site.register(City, CityAdmin)
admin.site.unregister(Region)
admin.site.register(Region, RegionAdmin)
admin.site.unregister(Country)
admin.site.register(Country, CountryAdmin)
admin.site.unregister(District)
admin.site.register(District, DistrictAdmin)
