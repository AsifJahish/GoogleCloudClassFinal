from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:user_id>/', views.user_update, name='user_update'),

    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/create/', views.notification_create, name='notification_create'),
    path('notifications/<int:pk>/edit/', views.notification_update, name='notification_update'),
    path('notifications/<int:pk>/delete/', views.notification_delete, name='notification_delete'),
]
