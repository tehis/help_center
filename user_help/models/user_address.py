import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField

from .custom_user import CustomUser


class CreatorType(models.TextChoices):
    USER = 'USR', _('User')
    SUPPORTER = 'SUP', _('Supporter')


class UserAddress(models.Model):
    class Meta:
        verbose_name = 'User Address'

    title = models.CharField(max_length=50, blank=True, default='')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(
        max_length=3, choices=CreatorType.choices, default=CreatorType.USER
    )
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [
        'title', 'location', 'user'
    ]

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + \
            self.title
