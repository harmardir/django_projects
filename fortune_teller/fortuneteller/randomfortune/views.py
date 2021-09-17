from django.shortcuts import render

# Create your views here.
# 01- Define a function that takes one parameter request and returns render function with 2 parameters request and path


def fortune(request):
    return render(request,"randomfortune/fortune.html")
