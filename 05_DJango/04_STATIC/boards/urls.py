from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='boards'

urlpatterns = [
    path('',views.index, name="index"),
    path('registerfrm/', views.registerfrm, name="registerfrm"),
    path('register/', views.register, name="register"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('updatefrm/<int:pk>', views.updatefrm, name="updatefrm"),
    path('update/<int:pk>', views.update, name="update"),
]