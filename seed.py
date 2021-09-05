import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant.settings')
django.setup()


from users.models import *
from finance.models import *
from kitchen.models import *
from service.models import *

