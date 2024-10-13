set -euxo pipefail

python manage.py migrate
python manage.py loaddata data/test_data.json
gunicorn --workers 2 mental_health_wait_times.wsgi