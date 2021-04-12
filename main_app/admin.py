from django.contrib import admin
from .models import Run, Pkinfo, Pokemon

# Register your models here.
admin.site.register(Run)
admin.site.register(Pokemon)
admin.site.register(Pkinfo)
