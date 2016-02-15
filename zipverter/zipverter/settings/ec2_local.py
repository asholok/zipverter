DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djgeo',
        'USER': 'asholok',
        'PASSWORD': 'asholok',
        'HOST': os.getenv('ZIPVERTER_RDS', ''),
        'PORT': '5432',
    }
}