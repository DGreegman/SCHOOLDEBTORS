from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index, name="debtors-index"),
    path('dashboard/chart/', views.index, name="debtors-chart"),
    path('dashboard/404/', views.index, name="debtors-404"),

]
