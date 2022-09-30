from dataclasses import field
from rest_framework import serializers
from apps.api.models import *


class UserBasicDataSerializer(serializers.ModelSerializer):
    image_field = serializers.FileField()
    password = serializers.CharField()

    class Meta:
        model = BasicData
        fields = ('first_name', 'last_name',
                  'email', 'password', 'document', 'image_field')

    def create(self, validated_data):
        image = validated_data.pop('image_field')
        user = self.context['request'].user.basic_data_admin
        image = "hola mundo"
        basic_data = super().create(validated_data)
        basic_data.set_password(validated_data['password'])
        basic_data.save()
        Leader.objects.create(image=image, admin=user, basic_data=basic_data)
        return basic_data

class LeaderDataSerializer():
    class Meta:
        model = Leader
        fields = '__all__'

class ReadBasicDataSerializer(serializers.ModelSerializer):
    basic_data_leader = LeaderDataSerializer()
    class Meta:
        model = BasicData
        exclude = ('password',)


        
