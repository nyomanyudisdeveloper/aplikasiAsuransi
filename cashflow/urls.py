from django.urls import path

from . import  views

app_name = 'cashflow'

urlpatterns = [
    path("premi",views.index, name="index"),
]

