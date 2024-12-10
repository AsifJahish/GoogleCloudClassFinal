from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.payment_list, name='payment_list'),
    path('create/', views.make_payment, name='make_payment'),
    path('<int:pk>/', views.payment_detail, name='payment_detail'),
]
