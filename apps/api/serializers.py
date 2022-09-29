from rest_framework import serializers
from apps.api.models import *


class UserLeaderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=25)
    email = serializers.EmailField()
    password1 = serializers.CharField(max_length=45)
    password2 = serializers.CharField(max_length=45)
    image_field = serializers.FileField()

    class Meta:
        model = Leader
        exclude = ('basic_data', 'admin', 'image')

    def create(self, validated_data):
        image = validated_data.pop('image_field')
        image = "hola mundo"
        admin = self.request.user
        basic_data = BasicData.objects.create(validated_data)
        return super().create(basic_data=basic_data, admin=admin, image=image)
