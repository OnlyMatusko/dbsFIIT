from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('v1/health', views.time, name='time'),
    path('v2/health', views.time2, name='time2'),
]