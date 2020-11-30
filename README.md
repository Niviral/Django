Simple basic Django (3.1.2) project created for learning purpose.

Project created with use of [SB Admin 2](https://startbootstrap.com/themes/sb-admin-2/) open source admin dashboard theme for [Bootstrap](https://getbootstrap.com/) created by [Start Bootstrap](https://startbootstrap.com/).

All application needed for project to work are docker containers for easy deployment.</br>
All `docker-compose.yml` and `.env` example file provided.

Before deployment please export Django Secret key to your enviroment variable:</br>
```export DJANGO_SECRET=="$(python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())')"```