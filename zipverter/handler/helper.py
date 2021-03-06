#!/usr/bin/python
# -*- coding: utf-8 -*-

from cities.models import City, PostalCode
from django.contrib.gis.measure import D
from django.db.models import Q
from handler.models import LocationTable
from handler.constants import BRAZILIAN_STATE_CODES_REAL, BRAZILIAN_STATE_CODES_REVERCE, SUITABLE_CITY_NAMES
import csv

def _get_region_filter(country_name, region_code):
    if region_code:
        if country_name == 'Brazil':
            if region_code in BRAZILIAN_STATE_CODES_REAL:
                return Q(region__code=BRAZILIAN_STATE_CODES_REAL[region_code])
        if country_name == 'United States':
            return Q(region__code=region_code)
    return Q()

def _get_city(city_name, country_name, region_code):
    region_filter = _get_region_filter(country_name, region_code)
    city_name = SUITABLE_CITY_NAMES[city_name] if city_name in SUITABLE_CITY_NAMES else city_name
    try:
        city_filter = Q(name__iexact=city_name, country__name=country_name)
        return City.objects.get(city_filter, region_filter)
    except City.DoesNotExist:
        city_filter = Q(name_std__iexact=city_name, country__name=country_name)
        return City.objects.get(city_filter, region_filter)
    except City.MultipleObjectsReturned:
        return City.objects.filter(city_filter, region_filter).order_by('-population')[0]
    except Exception, e:
        pass
    return False

def _create_response_list(neighborhood_list, country_name, region_code):
    city_name_list = []

    for city in neighborhood_list.filter(country__name=country_name): # for a case if radius crossed the border 
        city_region_code = city.region.code
        if country_name == 'Brazil':
            city_region_code = BRAZILIAN_STATE_CODES_REVERCE[city_region_code]
        city_name_list.append(city.name + ', ' + city_region_code if region_code else city.name) 
    return city_name_list

def get_cities_neighbor(city_name, country_name, measurement, radius, region_code):
    if country_name == 'Mexico': # TODO: Delete this after Mexico database corrected
        return []
    try:
        city = _get_city(city_name, country_name, region_code)
        if city:
            distance = D(mi=radius) if measurement == 'miles' else D(km=radius)
            neighborhood_list = City.objects.filter(location__distance_lte=(city.location, distance)).distinct()
            return _create_response_list(neighborhood_list, country_name, region_code)
        return 0
    except Exception, e:
        return False


def get_zipcode_neighbor(zip_code, country_name, measurement, radius):
    try:
        zip_objs = PostalCode.objects.filter(code=zip_code, country__name=country_name)
        if zip_objs:
            distance = D(mi=radius) if measurement == 'miles' else D(km=radius)
            neighborhood_list = PostalCode.objects.filter(location__distance_lte=(zip_objs[0].location, distance)).distinct()
            return list(set([zip_obj.code for zip_obj in neighborhood_list]))
        return 0
    except:
        return False        


def get_cities_by_population(country_name, population_min, population_max=0):
    city_filter = Q(country__name=country_name, population__gte=population_min)
    if population_max:
        city_filter &= Q(population__lte=population_max)
    
    cities = City.objects.filter(city_filter).order_by('population').values('name_std', 'name', 'population')
    with open(country_name + '_cities_+' + str(population_min), 'wb') as file:
        fieldnames = ['population', 'name', 'name_std']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for city in cities:
            city['name'] = unicode(city['name']).encode("utf-8")
            writer.writerow(city)
