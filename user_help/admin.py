from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserAddress


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = (
#         'id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active'
#     )
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {
#             'fields': ('id', 'password')
#         }),
#         ('Personal info', {
#             'fields': ('email', 'first_name', 'last_name', 'phone_number')
#         }),
#         ('Permissions', {
#             'fields': ('is_staff', 'is_active')
#         }),
#         ('Important dates', {
#             'fields': ('updated_at', 'last_login', 'date_joined')
#         }),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email', 'phone_number' 'password1', 'password2',
#                 'first_name', 'last_name', 'is_staff', 'is_active'
#             )}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


admin.site.register(CustomUser)
admin.site.register(UserAddress)
