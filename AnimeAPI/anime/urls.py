from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('latest', views.latest, name='latest'),
    path('detail/<str:vid_id>', views.details, name='details'),

]
