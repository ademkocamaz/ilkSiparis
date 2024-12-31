from django.contrib import admin

from baton.models import BatonTheme

admin.site.unregister(BatonTheme)
