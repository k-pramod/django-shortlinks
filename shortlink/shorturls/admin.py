from django.contrib import admin

# Register your models here.

from .models import Shortlink

class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shortlink, LinkAdmin)
