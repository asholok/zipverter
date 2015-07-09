import os 
from django.core.wsgi import get_wsgi_application
from whitenoise.dgango import DjangoWhiteNoise

os.environ["DJANGO_SETTINGS_MODULE"] = "zipverter.settings"
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
