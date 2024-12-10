from django.db import models

# Create your models here.
from django.db import models
from events.models import Registration  # Assuming Registration is in the `events` app

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} - {self.get_status_display()}"

    def is_successful(self):
        return self.status == 'COMPLETED'
