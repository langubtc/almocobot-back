from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Place

def place_list(request):
    objectQuerySet = Place.objects.order_by('placename')
    places = serializers.serialize("json", objectQuerySet, fields=('placename','address'))
    return JsonResponse(places, safe=False)