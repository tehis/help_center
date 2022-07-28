from dataclasses import dataclass

from django.db.models import Count

from user_help.models import CustomUser


def get_user_with_addresses_count():
    return CustomUser.objects.annotate(addresses_count=Count('useraddress'))
