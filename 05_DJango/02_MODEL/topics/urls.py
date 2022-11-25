from django.urls import path
from . import views

app_name = "topics"

urlpatterns = [
    path('index/', views.index, name='index'),
]