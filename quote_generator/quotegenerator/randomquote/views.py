from django.shortcuts import render

def quote(request):
    return render(request,"randomquote/quote.html")