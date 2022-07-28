from dataclasses import fields

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from user_help.helpers.send_notif import send_notif
from user_help.models import CustomUser
from user_help.models.user_address import CreatorType, UserAddress


class PublicUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class PublicUserProfileForSupportersSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    addresses_count = serializers.IntegerField()
    last_address = serializers.CharField(max_length=150)


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['user', 'title', 'location']

    def create(self, validated_data):
        send_notif(validated_data['title'], validated_data['user'])
        user_object = UserAddress.objects.create(**validated_data)
        validated_data['created_by'] = CreatorType.SUPPORTER
        return user_object
