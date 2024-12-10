from django.db import models

# Create your models here.
from django.db import models
from users.models import User  # Assuming the User model is in the 'users' app
# models.py
from django.db import models
from users.models import User  # Adjust the import according to your User model's location

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registration_date = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=50)
    number_of_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.event.title}"

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} ticket for {self.event.title}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class EventCategory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='event_categories')

    def __str__(self):
        return f"{self.event.title} - {self.category.name}"
