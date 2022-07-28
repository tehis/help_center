from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_help.serializers import UserAddressSerializer

@csrf_exempt
@api_view(['POST'])
def add_user_address(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    print('request body: ')
    print(request.data)

    serializer = UserAddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
