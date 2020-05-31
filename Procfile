web: gunicorn wonya.wsgi --log-file -
release: python -m pip uninstall pillow
release: python -m pip install pillow
release: python manage.py makemigrations
release: python manage.py migrate
