from django.contrib import admin

from . import models

admin.site.register(models.Claim)
admin.site.register(models.Email)
