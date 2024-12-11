from django.contrib import admin

from .models import User, Notification
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Notification)
