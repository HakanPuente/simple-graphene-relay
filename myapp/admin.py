from django.contrib import admin
from myapp.models import Model1A

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Model1A) 