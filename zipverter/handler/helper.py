# coding=utf-8
from cities.models import City
from django.contrib.gis.measure import D
from django.db.models import Q

def get_city(city_name, country_name):
    try:
        city_filter = Q(name=city_name, country__name=country_name)
        return City.objects.get(city_filter)
    except City.DoesNotExist:
        city_filter = Q(name_std=city_name, country__name=country_name)
        return City.objects.get(city_filter)
    except City.MultipleObjectsReturned:
        return City.objects.filter(city_filter).order_by('-population')[0]
    except Exception, e:
        pass
    return False

def get_cities_neighbor(city_name, country_name, measurement, radius):
    try:
        city = get_city(city_name, country_name)
        if city:
            distance = D(mi=radius) if measurement == 'miles' else D(km=radius)
            neighborhood_list = City.objects.filter(location__distance_lte=(city.location, distance))
            return [city.name for city in neighborhood_list]
        return 0
    except Exception, e:
        return False
        
