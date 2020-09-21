from django.contrib import admin
from .models import Gallery, categories, location

# Register your models here.

admin.site.register(Gallery)
admin.site.register(categories)
admin.site.register(location)