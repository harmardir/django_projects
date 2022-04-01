from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from pyrsistent import v

from .models import Book , Author , Publisher

def setup(request):
    a1 = Author.objects.create(name='Curie')
    a2 = Author.objects.create(name='Ramanujan')
    a3 = Author.objects.create(name='Abdusalam')
    a4 = Author.objects.create(name='Finstein')
    
    p1 = Publisher.objects.create(name ='Lebanese Publishing House')
    p2 = Publisher.objects.create(name = 'Fantastic Books')
    p3 = Publisher.objects.create(name ='SciBooks')

    b1 = Book(title = 'Python Programming',
              price = 230,
              field = 'Computer Science',
              publication_date = '2020-10-10',
              publisher = p1)
    b1.suathors__set = a1
    b1.save()

    b2 = Book(title = 'Django Security',
              price = 110,
              field = 'Cybersecurity',
              publication_date = '2019-03-05',
              publisher = p2)
    b2.save()
    b2.authors.add(a2,a3,a4)

    b3 = Book(title = 'Machine Learning',
              price = 110,
              field = 'Data Science',
              publication_date = '2020-10-10',
              publisher = p3)
    b3.save()          
    b3.authors.add(a1,a3)
    
    return HttpResponse('Setup done!')


def index(request):
    results = Book.objects.all()
    #get() expects a keyword argument, it only returns a single object 
    # Most basic keyword argument: field__lookuptype=value
    results = Book.objects.get(id=2)
    return render(request, 'main/index.html', {'results': results})


