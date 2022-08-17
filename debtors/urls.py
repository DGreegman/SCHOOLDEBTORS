from django.urls import path 
from . import views



urlpatterns = [
    path('dashboard/', views.index, name="debtors-index"),
    path('dashboard/chart/', views.chart, name="debtors-chart"),
    path('dashboard/404/', views.page404, name="debtors-404"),
    path('dashboard/sign-in/', views.signin, name="debtors-signin"),
    path('dashboard/sign-up/', views.signup, name="debtors-signup"),

]
