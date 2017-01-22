from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.Serializer):
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