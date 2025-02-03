from django.urls import path
from .views import (
    CategoryListView, PlantListView, UserCreateView, UserLoginView,
    PlantCategoryListCreateView, PlantCategoryDetailView,
    PlantListCreateView, PlantDetailView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('categories/', PlantCategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', PlantCategoryDetailView.as_view(), name='category-detail'),
    path('plants/', PlantListCreateView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('plants/list/', PlantListView.as_view(), name='plant-list_view'),
    path('categories/list/', CategoryListView.as_view(), name='category-list_view'),
    
]