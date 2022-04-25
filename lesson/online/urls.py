from django.urls import path
from .views import *

urlpatterns = [
    path('',news,name='news'),
    path('category/<int:id>/',cats,name='cats'),
    path('search/',search,name='search'),
    path('forms/',add,name='forms'),
    path('info/<int:id>/',info,name='info'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]