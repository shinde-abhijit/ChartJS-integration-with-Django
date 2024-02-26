from django.urls import path, include
from chart import views
urlpatterns = [
    path('', views.home, name='home'),
]
