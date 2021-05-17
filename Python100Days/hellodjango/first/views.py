from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    fruits = ['Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry', 'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango']
    return HttpResponse(fruits)