import os
from base import *

ENVIRONMENT_ID = os.getenv('DJANGO_ENV', '')

if ENVIRONMENT_ID == 'PROD':
    from ec2_local import *
