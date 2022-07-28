from user_help.models import CreatorType, UserAddress


def get_user_addresses(created_by: CreatorType) -> None:
    return UserAddress.objects.filter(created_by=created_by).values()
