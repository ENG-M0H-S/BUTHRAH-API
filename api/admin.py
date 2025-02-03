from django.contrib import admin
from api.models import User, Plant, PlantCategory
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(PlantCategory)
admin.site.register(Plant)