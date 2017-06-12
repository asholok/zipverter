"""zipverter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from APIs.city_response import ZipTableResource, CitysNeighborhoodResource, PostalCodeNeighborhoodResource, CitiesResource, \
    DistrictResource
from django.views.generic import TemplateView
from handler.models import LoggForLocationTable
from handler.views import LoggView
from tastypie.api import Api
# import debug_toolbar

# zip_convertor_resource = ZipTableResource()
rest_api = Api(api_name='api')
rest_api.register(CitiesResource())
rest_api.register(DistrictResource())
rest_api.register(ZipTableResource())
rest_api.register(CitysNeighborhoodResource())
rest_api.register(PostalCodeNeighborhoodResource())

urlpatterns = [
    url(r'', include(rest_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logs/', LoggView.as_view(), name='logs'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]
