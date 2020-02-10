#!/usr/bin/python3
#Created By: JMedlock
#Created On: 2/6/20

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]

