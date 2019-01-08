import json

from django.http import HttpResponse
from restraurant.models import Restaurant
from django.shortcuts import render

# Create your views here.
def index(request):
    response1 = ""

    # list = Restaurant.objects.order_by('name')[0:2]
    data = Restaurant.objects.filter(name__contains="Roc")
    # for p in list:
    #     response1 += p.name +" "+p.price_range+ "<br>"
    # response = response1

    for i in data:
        response1 +=i.name

    content = {"data" : response1}

    print(response1)
    return render(request, "index.html",content)
