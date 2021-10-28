from django.contrib import admin
from django.urls import path
from epics import views

urlpatterns = [
    path('all/', views.GetAllEpics.as_view()),
]
