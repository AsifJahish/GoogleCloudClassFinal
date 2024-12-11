from django.contrib import admin

# Register your models here.
from .models import Event, Registration, EventCategory, Category, Ticket, Review
from django.contrib import admin

# Register your models here.
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(EventCategory)
admin.site.register(Category)
admin.site.register(Ticket)
admin.site.register(Review)
