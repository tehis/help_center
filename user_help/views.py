import json
from typing import Dict, List

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_help.helpers.get_users_with_addresses_count import \
    get_users_with_addresses_count
from user_help.models.user_address import UserAddress
from user_help.serializers import (PublicUserProfileForSupportersSerializer,
                                   UserAddressSerializer)


@csrf_exempt
@api_view(['POST'])
def add_user_address(request):
    serializer = UserAddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def get_users_list(request):
    users = get_users_with_addresses_count()
    data: List[Dict] = []

    for user in users:
        data.append({})
        data[-1]['first_name'] = user.first_name
        data[-1]['last_name'] = user.last_name
        data[-1]['addresses_count'] = user.addresses_count
        data[-1]['last_address'] = \
            UserAddress.objects.filter(user_id=user.id).latest('created_at')

    serializer = PublicUserProfileForSupportersSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
