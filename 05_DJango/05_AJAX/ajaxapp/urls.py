from django.urls import path
from . import views

urlpatterns = [
    path('ajaxfrm/', views.ajaxfrm, name='ajaxfrm'),
    path('ajaxmeet/', views.ajaxmeet, name='ajaxmeet'),
    path('ajaxschedule/', views.ajaxschedule, name='ajaxschedule')
]
