from cities.models import City, PostalCode, Country, District
import requests
import json


def formatize_results(obj):
    return {'state': obj.region.name, 'state_code': obj.region.code, 'city': obj.name}

def get_postmon_results(zip_code):
    try:
        response = requests.get('http://api.postmon.com.br/v1/cep/' + zip_code)
        result = json.loads(response.text)
        return {
                    'state': result['estado_info']['nome'], 
                    'state_code': result['estado'], 
                    'city': result['cidade'],
                    'district': result['bairro']
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
                names = zip_objs[0].names
                return {'state': names[1], 'state_code': '', 'city': names[3]}
            except:
                return None
        return formatize_results(City.objects.distance(zip_objs[0].location).order_by('distance')[0])
    return None
    