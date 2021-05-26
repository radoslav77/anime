from django.urls import path

from . import views

urlpatterns = [
    path('', views.latest, name='latest'),
    path('detail/<str:vid_id>', views.details, name='details'),
    path('search', views.search, name='search'),

]
