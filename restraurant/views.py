import json

from django.http import HttpResponse
from restraurant.models import Restaurant
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
def index(request):
    # all = Restaurant.objects.all()
    # data = []
    # for i in all:
    #     temp = [i.name, i.phone, i.food_review, i.ambience_review, i.google_map,i.latitude]
    #     data.append(temp)

    content = {}

    return render(request, "table.html", content)


@csrf_exempt
def main_table(request):
    Restuarant_type = request.POST['Restuarant_type']
    Restuarant_sort = request.POST['Restuarant_sort']
    print(Restuarant_sort + "  " + Restuarant_type)

    all = Restaurant.objects.all()
    res = Restaurant.objects.filter(restaurant_type=Restuarant_type).order_by("-" + Restuarant_sort)

    data = []

    for i in res:
        temp = {}
        temp['name'] = i.name
        temp['type'] = i.restaurant_type
        temp['add'] = i.street_address
        temp['info'] = i.description
        temp['phone'] = i.phone
        if Restuarant_sort == "average_review":
            temp['star'] = i.average_review
        elif Restuarant_sort == "food_review":
            temp['star'] = i.food_review
        elif Restuarant_sort == "service_review":
            temp['star'] = i.service_review
        elif Restuarant_sort == "ambience_review":
            temp['star'] = i.ambience_review
        elif Restuarant_sort == "value_review":
            temp['star'] = i.value_review

        temp['web'] = i.website
        temp['map'] = "https://"+i.google_map
        data.append(temp)

    content = {"data": data}

    return render(request, "small_table.html", content)


@csrf_exempt
def sectable(request):
    search = request.POST['searchTEXT']
    print(search)
    data = []
    if (search != ""):
        res = Restaurant.objects.filter(name__contains=search)
        for i in res:
            temp = {}
            temp['name'] = i.name
            temp['type'] = i.restaurant_type
            temp['add'] = i.street_address
            temp['phone'] = i.phone
            temp['web'] = i.website
            data.append(temp)

    content = {"data": data}

    return render(request, "tiantable.html", content)
