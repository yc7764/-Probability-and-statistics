from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name="index"),
    path('registerfrm/', views.registerfrm, name="registerfrm"),
    path('register/', views.register, name="register"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('post', views.UploadImage.as_view(), name="post"),
]
