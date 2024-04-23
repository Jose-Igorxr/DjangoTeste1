from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView, DetailView, UpdateView




class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    template_name ='meu_modelo/post_create.html'
    success_url = '/posts/'

class PostDetailView(DetailView):
    model = Post
    template_name = 'meu_modelo/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'meu_modelo/post_update.html'
    success_url = '/posts/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'meu_modelo/post_delete.html'
    success_url = reverse_lazy('post_list')

class PostListView(ListView):
    model = Post
    template_name = 'meu_modelo/post_list.html'
    context_object_name = 'posts'



