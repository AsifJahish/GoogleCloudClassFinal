from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration, Review, Ticket
from .forms import EventForm, RegistrationForm, ReviewForm, TicketForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    registrations = Registration.objects.filter(event=event)
    reviews = Review.objects.filter(event=event)
    tickets = Ticket.objects.filter(event=event)
    return render(request, 'event_detail.html', {'event': event, 'registrations': registrations, 'reviews': reviews, 'tickets': tickets})


# views.py
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from .forms import RegistrationForm

from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm

def register_for_event(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)  # Don't save to the database yet
            registration.user = form.cleaned_data['user']  # Set the user from form.cleaned_data
            registration.save()  # Save the instance to the database
            return redirect('event_list')  # Redirect after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # Don't save to the database yet
            review.user = form.cleaned_data['user']  # Set the user from form.cleaned_data
            review.save()  # Save the instance to the database
            return redirect('event_detail', pk=review.event.pk)  # Redirect to the event's detail page
    else:
        form = ReviewForm()

    return render(request, 'review_form.html', {'form': form})
