from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('addOne', views.addOne, name='addOne'),
]