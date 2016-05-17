# coding=utf-8
from cities.models import City, PostalCode, Country, District
import requests
import json


def formatize_results(obj):
    return {
                'state': obj.region.name, 
                'state_code': obj.region.code, 
                'city': obj.name, 
                'timezone': obj.timezone
            }

def get_postmon_results(zip_code):
    try:
        response = requests.get('http://api.postmon.com.br/v1/cep/' + zip_code)
        result = json.loads(response.text)
        try:
            timezone = City.objects.get(name=unicode(result['cidade']), country__name='Brazil').timezone
        except:
            timezone = ''
        state = result['estado_info']['nome'] if result.get('estado_info', False) else ''
        return {
                    'state': state, 
                    'state_code': result['estado'], 
                    'city': result['cidade'],
                    'district': result['bairro'],
                    'timezone': timezone
                }
    except:
        pass
    return None

def find_location_info(zip_code, country_name):
    if country_name == 'Brazil':
        return get_postmon_results(zip_code)
    zip_objs = PostalCode.objects.filter(code=zip_code, country__name=country_name)

    if zip_objs:
        if country_name == 'Mexico':
            try:
                zip_obj = zip_objs[0]
                district_name = zip_obj.district_name
                city_name = district_name if district_name else zip_obj.subregion_name
                city_obj = City.objects.distance(zip_obj.location).order_by('distance')[0]
                
                return {
                            'state': zip_obj.region_name, 
                            'state_code': '', 
                            'city': city_name, 
                            'timezone': city_obj.timezone
                        }
            except Exception, e:
                print e
                return None
        return formatize_results(City.objects.distance(zip_objs[0].location).order_by('distance')[0])
    return None
    