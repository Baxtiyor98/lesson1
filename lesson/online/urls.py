from django.urls import path
from .views import *

urlpatterns = [
    path('news/',news,name='news'),
    path('forms/',add,name='forms'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]