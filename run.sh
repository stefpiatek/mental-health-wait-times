set -euxo pipefail

python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata data/test_data.json
python3 -m gunicorn --workers 2 mental_health_wait_times.wsgi
