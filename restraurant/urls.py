from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('maintable',views.main_table)

]