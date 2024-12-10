from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/edit/', views.event_update, name='event_update'),



    path('register/', views.register_for_event, name='register_form'),
    path('review/', views.add_review, name='review_form'),
    # path('<int:pk>/register/', views.register_for_event, name='register_for_event'),
    # path('<int:pk>/review/', views.add_review, name='add_review'),
]
