from django.shortcuts import render
from matplotlib.style import context
from django.http import JsonResponse
import random

# Create your views here.
def index(request):
    return render(request, "index.html")

def variables(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'James',
    }
    context = {
        'foods': foods,
        'info': info
    }
    return render(request, "variables.html", context)

def filters(request):
    foods = ['스파게티', '라면', '우동', '짜장면', '짬뽕']
    pick = random.choice(foods)

    context = {
        'foods': foods,
        'pick': pick
    }
    return render(request, "filters.html", context)

def form(request):
    return render(request, "form.html")

def result(request):
    message = request.GET.get("message")
    
    context = {
        'message': message
    }
    return render(request, "result.html", context)

def ajaxfrm(request):
    return render(request, "ajaxfrm.html")

def ajax(request):
    id = request.GET.get("userId")

    if id=="django":
        context = {
            'login': "django!! Login OK"
        }
    else:
        context = {
            'login': "login Fail!! Try Again~!!"
        }
    return JsonResponse(context)

def varRoute(request, name):
    context ={
        'name': name,
    }
    return render(request, "varRoute.html", context)