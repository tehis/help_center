from dataclasses import fields
from rest_framework import serializers
from user_help.models import CustomUser
from user_help.models.user_address import UserAddress
from user_help.helpers.send_notif import send_notif


class PublicUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']

    # def create(self, validated_data):
    #     obj = super().create(validated_data)

    #     obj.save()
    #     return obj

    # def update(self, instance, validated_data):
    #     obj = super().update(instance, validated_data)
    #     obj.save()
    #     return obj

class PublicUserProfileForSupportersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['user', 'title', 'location']

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.save()
        send_notif(validated_data['title'], validated_data['user'])
        return obj
