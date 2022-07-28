from django.urls import path
from user_help import views


urlpatterns = [
    path('add-address', views.add_user_address, name='Add Address'),
]