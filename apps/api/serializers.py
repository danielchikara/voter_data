from rest_framework import serializers
from apps.api.models import *


class BasicLeaderDataSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = BasicData
        exclude = ('password', 'email')


class BasicVoterDataSerializer(serializers.ModelSerializer):
    polling_station = serializers.IntegerField()
    neighborhood = serializers.IntegerField()
    address = serializers.CharField(max_length=50)

    class Meta:
        model = BasicData
        fields = ('first_name', 'last_name',
                  'email',  'document', 'polling_station', 'neighborhood', 'address')

    def create(self, validated_data):
        polling_station = validated_data.pop('polling_station')
        neighborhood = validated_data.pop('neighborhood')
        address = validated_data.pop('address')
        user = self.context['request'].user.basic_data_leader
        basic_data = super().create(validated_data)
        polling_station = PollingStation.objects.get(id=polling_station)
        neighborhood = Neighborhood.objects.get(id=neighborhood)
        Voter.objects.create(leader=user, basic_data=basic_data,
                             polling_station=polling_station, neighborhood=neighborhood, address=address)

        return basic_data
