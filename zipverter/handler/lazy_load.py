from cities.models import City, PostalCode


def find_city(zip_code, country_name):
    zip_objs = PostalCode.objects.filter(code=zip_code, country__name=country_name)

    for zip_obj in zip_objs:
        city = City.objects.distance(zip_obj.location).order_by('distance')[0]

        return city.name

    return False

