from django.urls import path, re_path
from .import views

app_name = 'Highcharts'

urlpatterns = [
    path('', views.home, name='home'),
    # path('visualize/', views.visualize, name='visualize'),
]