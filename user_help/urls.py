from django.urls import path

from user_help import views

urlpatterns = [
    path('add-address/', views.add_user_address, name='Add Address'),
    path('users/', views.get_users_list, name='User Lists')
]