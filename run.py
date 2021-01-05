from os import system
import sys 
try:
   menu = sys.argv[1]
   if menu == 'runserver':
       system('python manage.py runserver 7000')
   elif menu == 'shell':
        system('python manage.py shell')
   elif menu == 'createsuperuser':
         system('python manage.py createsuperuser')
   elif menu == 'migrate':
        system('python manage.py makemigrations && python manage.py migrate')
   else: 
        system('python manage.py runserver 7000')
except IndexError:
       system('python manage.py runserver 7000')