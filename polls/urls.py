from django.urls import path

from . import views

urlpatterns = [
    #path('', views.mainpage, name='mainpage'),
    path('', views.DesieseView.as_view()),
    #path('code.py', views.DesieseView.answ)
]