from rest_framework import serializers
from .models import Place, User, UserPlace

class PlaceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    placename = serializers.CharField(max_length=500)
    address = serializers.CharField(required=False, allow_blank=True, max_length=500)

    def create(self, validated_data):
        """
        Create and return a new `Place` instance, given the validated data.
        """
        return Place.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Place` instance, given the validated data.
        """
        instance.placename = validated_data.get('placename', instance.placename)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    userId = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.userId = validated_data.get('userId', instance.userId)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class UserPlaceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    userId = serializers.CharField(max_length=200)
    placeId = serializers.CharField(max_length=100)
    fav = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `UserPlace` instance, given the validated data.
        """
        validated_data['userId'] = User.objects.get(userId=validated_data['userId'])
        validated_data['placeId'] = Place.objects.get(id=validated_data['placeId'])
        return UserPlace.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserPlace` instance, given the validated data.
        """
        validated_data['userId'] = User.objects.get(userId=validated_data['userId'])
        validated_data['placeId'] = Place.objects.get(id=validated_data['placeId'])

        instance.userId = validated_data.get('userId', instance.userId)
        instance.placeId = validated_data.get('placeId', instance.placeId)
        instance.fav = validated_data.get('fav', instance.fav)
        instance.save()
        return instance