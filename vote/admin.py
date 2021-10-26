from django.contrib import admin

from .models import Sondage
admin.site.register(Sondage)

from .models import Member
admin.site.register(Member)
