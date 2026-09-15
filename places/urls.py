from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.place_list, name='list'),
    path('places/add/', views.add_place, name='add'),
    path('places/<int:place_id>/', views.place_detail, name='detail'),
]
