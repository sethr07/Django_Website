from django.urls import path
from rsPortfolio import views

urlpatterns = [
    path('', views.hello_world, name='rsPortfolio'),
]
