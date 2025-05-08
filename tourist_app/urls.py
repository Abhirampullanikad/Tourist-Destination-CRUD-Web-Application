from django.contrib import admin
from django.urls import path
from .views import *
from .import views

urlpatterns = [
        path('DestinationCreate/', DestinationListCreateAPIView.as_view(), name='destination-list-create'),
        path('DestinationDetail/<int:pk>/',DestinationDetail.as_view(),name='destination-detail'),
        path('DestinationUpdate/<int:pk>/',DestinationUpdateView.as_view(),name='destination-update'),
        path('Destinationdelete/<int:pk>/',DestinationDelete.as_view(),name='destination-delete'),
        path('Destinationsearch/<int:pk>/',DestinationSearch.as_view(),name='destination-search'),
        
        path('', views.destination_list, name='destination_list'),
        path('create/', views.destination_create, name='destination_create'),
        path('destination_detail/<int:pk>/', views.destination_detail, name='destination_detail'),
        path('destination_update/<int:pk>/', views.destination_update, name='destination_update'),
        path('destination_delete/<int:pk>/', views.destination_delete, name='destination_delete'),
        path('search/', views.destination_search, name='destination_search'),


]
