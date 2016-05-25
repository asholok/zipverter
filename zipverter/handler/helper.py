# coding=utf-8
from cities.models import City
from django.contrib.gis.measure import D
from django.db.models import Q
from handler.models import LocationTable
from handler.constants import BRAZILIAN_STATE_CODES_REAL, BRAZILIAN_STATE_CODES_REVERCE

def get_region_filter(country_name, region_code):
    if region_code:
        if country_name == 'Brazil':
            region_code = BRAZILIAN_STATE_CODES_REAL[region_code]
        return Q(region__code=region_code)
    return Q()

def get_city(city_name, country_name, region_code):
    region_filter = get_region_filter(country_name, region_code)
    try:
        city_filter = Q(name=city_name, country__name=country_name)
        return City.objects.get(city_filter, region_filter)
    except City.DoesNotExist:
        city_filter = Q(name_std=city_name, country__name=country_name)
        return City.objects.get(city_filter, region_filter)
    except City.MultipleObjectsReturned:
        return City.objects.filter(city_filter, region_filter).order_by('-population')[0]
    except Exception, e:
        pass
    return False

def create_response_list(neighborhood_list, country_name, region_code):
    city_name_list = []

    for city in neighborhood_list:
        city_region_code = city.region.code
        if country_name == 'Brazil':
            city_region_code = BRAZILIAN_STATE_CODES_REVERCE[city_region_code]
        city_name_list.append(city.name + ', ' + city_region_code if region_code else city.name) 
    return city_name_list

def get_cities_neighbor(city_name, country_name, measurement, radius, region_code):
    try:
        city = get_city(city_name, country_name, region_code)
        if city:
            distance = D(mi=radius) if measurement == 'miles' else D(km=radius)
            neighborhood_list = City.objects.filter(location__distance_lte=(city.location, distance))
            return create_response_list(neighborhood_list, country_name, region_code)
        return 0
    except Exception, e:
        return False
        
