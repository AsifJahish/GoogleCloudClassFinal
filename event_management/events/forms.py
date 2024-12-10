from django import forms
from .models import Event, Registration, Review, Ticket
from django import forms
from .models import Event
from django.forms import DateTimeInput

from django import forms
from .models import Registration, Event

from users.models import User
from django import forms
from .models import Event
from users.models import User

from django import forms
from .models import Review, Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'created_by']
        
    created_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        label='Event Creator',
        empty_label="Select a creator",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Date and time picker for the 'date_time' field
    date_time = forms.DateTimeField(
        required=True,
        widget=forms.widgets.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}
        ),
        label='Event Date and Time'
    )


from django import forms
from .models import Registration, User

class RegistrationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")  # Add user field

    class Meta:
        model = Registration
        fields = ['event', 'ticket_type', 'number_of_tickets', 'user']  # Include user explicitly


# forms.py

# forms.py

from django import forms
from .models import Event, Review

from django import forms
from .models import Review, User

class ReviewForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")  # Add user field

    class Meta:
        model = Review
        fields = ['event', 'rating', 'comment', 'user']  # Include user explicitly

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'type', 'price', 'availability']
