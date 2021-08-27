from django.urls import path
from . import views
app_name = 'operaciones'
urlpatterns = [
    path('',views.index,name='index'),
    path('solucion',views.solucion,name='solucion'),

]