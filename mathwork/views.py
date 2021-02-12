from django.http import HttpResponse
from django.shortcuts import render
from .models import MathQuestion

# Create your views here.


def index(request):
    import random
    a = MathQuestion()
    x = random.randint(1, 13)
    if x == 1:
        question = a.multiplication()
    elif x == 2:
        question = a.devision()
    elif x == 3:
        question = a.many_in()
    elif x == 4:
        question = a.shopping()
    elif x == 5:
        question = a.time_lap()
    elif x == 6:
        question = a.time_trip()
    elif x == 7:
        question = a.fraction()
    elif x == 8:
        question = a.time()
    elif x == 9:
        question = a.fraction_minus()
    elif x == 10:
        question = a.addition()
    elif x == 11:
        question = a.oporder()
    elif x == 12:
        question = a.ampm()
    else:
        question = a.time_home()
    return render(request, 'index_math.html', {'question': question})

