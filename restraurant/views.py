import json

from django.http import HttpResponse
from restraurant.models import Restaurant
from django.shortcuts import render

# Create your views here.
def index(request):




    all = Restaurant.objects.all()
    data = []
    for i in all:
        temp = [i.name, i.phone, i.food_review, i.ambience_review, i.google_map]
        data.append(temp)

    content = {"ps_data" : data}


    return render(request, "index.html", content)
