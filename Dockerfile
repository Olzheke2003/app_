FROM python:3.9

RUN mkdir app
WORKDIR /app
COPY . /app/

RUN pip install -r req.txt

CMD python manage.py migrate \
   && python manage.py loaddata request.json
   && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('root', 'admin@example.com', 'root')" \
   && python manage.py runserver 0.0.0.0:8000
