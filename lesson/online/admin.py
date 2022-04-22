from django.contrib import admin
from .models import News,Category,Regions

admin.site.register(Regions)
admin.site.register(Category)
admin.site.register(News)