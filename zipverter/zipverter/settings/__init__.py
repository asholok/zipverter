import os
from base import *

ENVIRONMENT_ID = os.getenv('DJANGO_ENV', '')

if ENVIRONMENT_ID == 'DEV':
    from ec2_local import *
