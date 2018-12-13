import os
import sys
sys.path.insert(0, "/var/www/mitchell/code/Sticker_Slab")
from django.core.wsgi import get_wsgi_application
os.environ["DJANGO_SETTINGS_MODULE"] = "Sticker_Slab.settings"
application = get_wsgi_application()