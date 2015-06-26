from cities.models import City, PostalCode


def find_city(zip_code, country_name):
    zip_objs = PostalCode.objects.filter(code=zip_code)
    cities = [City.objects.distance(zip_obj.location).order_by('distance')[0] for zip_obj in zip_objs]

    for city in cities:
        if city.country.name == country_name:
            return city.name

    return False

