from fortuneteller.fortuneteller.randomfortune.views import fortune
from django.urls import path
from . import views

urlpatterns = [path("",views.fortune)]