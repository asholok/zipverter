#!/bin/sh
export C_FORCE_ROOT=1
python manage.py migrate zipverter
python manage.py syncdb --noinput

supervisord -c supervisord.conf -n
