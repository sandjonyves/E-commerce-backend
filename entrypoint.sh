

set -e 

source /env/bin/activate

if [$1 == 'gunicorn'] : then

        exec gunicorn django_invoice.wsi:appliccation -b 0.0.0.0:8000


else

    exec python manage.py runserver 0.0.0.0:8000

fi