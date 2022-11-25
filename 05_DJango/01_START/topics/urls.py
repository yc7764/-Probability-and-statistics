from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('variables/', views.variables, name='variables'),
    path('filters/', views.filters, name='filters'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result'),
    path('ajaxfrm/', views.ajaxfrm, name='ajaxfrm'),
    path('ajax/', views.ajax, name='ajax'),

    #요청시 주소창으로 값을 동적으로 넘기는 방법
    path('varRoute/<str:name>', views.ajax, name='varRoute'),
]