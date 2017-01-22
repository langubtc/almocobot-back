from django.contrib import admin
from .models import User, Place, UserPlace

admin.site.register(User)
admin.site.register(Place)
admin.site.register(UserPlace)