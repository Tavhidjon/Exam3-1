from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Movie, Category, Show, Order

class BaseTemplateView(TemplateView):
    template_name='base.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'deadline', 'is_active', 'price', 'video', 'description']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['name',  'deadline', 'is_active', 'price', 'video', 'description']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'movie_id']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'movie_id']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class ShowListView(ListView):
    model = Show
    template_name = 'show_list.html'

class ShowCreateView(CreateView):
    model = Show
    fields = ['address', 'category_id']
    template_name = 'show_form.html'
    success_url = reverse_lazy('show_list')

class ShowUpdateView(UpdateView):
    model = Show
    fields = ['address', 'category_id']
    template_name = 'show_form.html'
    success_url = reverse_lazy('show_list')

class ShowDeleteView(DeleteView):
    model = Show
    template_name = 'show_confirm_delete.html'
    success_url = reverse_lazy('show_list')

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['show_id', 'user_id', 'amount', 'paying_by']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['show_id', 'user_id', 'amount', 'paying_by']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
