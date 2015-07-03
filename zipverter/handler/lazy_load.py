from cities.models import City, PostalCode

def find_city(zip_code, country_name):
    zip_objs = PostalCode.objects.filter(code=zip_code, country__name=country_name)
    if zip_objs:
        return City.objects.distance(zip_objs[0].location).order_by('distance')[0].name
    return False
    # try:
    #     zip_objs = PostalCode.objects.get(code=zip_code, country__name=country_name)
        
    #     return City.objects.distance(zip_obj.location).order_by('distance')[0].name
    # except PostalCode.DoesNotExist:
    #     return False

