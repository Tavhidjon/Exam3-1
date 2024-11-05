from django.urls import path
from .views import *

urlpatterns = [
    path('',BaseTemplateView.as_view(), name='base'),
    path('movies/',MovieListView.as_view(), name='movie_list'),
    path('movie/create/',MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/edit/',MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:pk>/delete/',MovieDeleteView.as_view(), name='movie_delete'),
    
    path('categories/',CategoryListView.as_view(), name='category_list'),
    path('category/create/',CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/',CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/',CategoryDeleteView.as_view(), name='category_delete'),
    
    path('shows/',ShowListView.as_view(), name='show_list'),
    path('show/create/',ShowCreateView.as_view(), name='show_create'),
    path('show/<int:pk>/edit/',ShowUpdateView.as_view(), name='show_edit'),
    path('show/<int:pk>/delete/',ShowDeleteView.as_view(), name='show_delete'),
    
    path('orders/',OrderListView.as_view(), name='order_list'),
    path('order/create/',OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit/',OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete/',OrderDeleteView.as_view(), name='order_delete'),
]
