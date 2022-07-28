from django.db import models
from .custom_user import CustomUser
from location_field.models.plain import PlainLocationField
import uuid
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils.translation import gettext_lazy as _


class UserAddress(models.Model):
    class Meta:
        verbose_name = 'User Address'

    class CreatorTtype(models.TextChoices):
        USER = 'USR', _('User')
        SUPPORTER = 'SUP', _('Supporter')

    title = models.CharField(max_length=50, blank=True, default='')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    creator_type = models.CharField(
        max_length=3, choices=CreatorTtype.choices, default=CreatorTtype.USER
    )
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [
        'title', 'location', 'user'
    ]

    def __str__(self):
        return self.title + " " + self.location