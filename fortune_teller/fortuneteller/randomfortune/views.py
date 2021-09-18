from django.shortcuts import render
import random

# Create your views here.
# 01- Define a function that takes one parameter request and returns render function with 2 parameters request and path
# 02- creating a list of fortunes named fortuneList inside our app’s views.py file. Define it outside of the fortune() function.
# 03- To select a random fortune from the list we’ll use a built-in Python function, random.choice().
# 04- Import the random module at the top of views.py. Then inside the fortune() function create a variable named fortune and set it equal to random.choice(fortuneList).
# 05-  To send teh fortune to the HTML template, we’ll create a context variable to send with the template.
# 06- create a dictionary named context. In the dictionary, create a key named "fortune" and set fortune as the value.
# 07- add our newly created context as the third argument to the render() function that fortune() returns.


def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}
    return render(request,"randomfortune/fortune.html", context)
    

fortuneList = [
   "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"
]
