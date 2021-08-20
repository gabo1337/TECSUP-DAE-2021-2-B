from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/<int:num1>/<int:num2>/', views.suma, name='sum'),
    path('resta/<int:num1>/<int:num2>/', views.resta, name='rest'),
    path('multiplicacion/<int:num1>/<int:num2>/', views.multiplicacion, name='mult'),
]