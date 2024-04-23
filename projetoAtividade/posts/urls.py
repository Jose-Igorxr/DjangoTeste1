from django.urls import path
from . import views

from .views import PostCreateView, PostDetailView,PostUpdateView, PostDeleteView, PostListView
urlpatterns = [
 path('', PostListView.as_view(), name='post_list'), #URL para listar todos os posts
 path('create/', PostCreateView.as_view(),
name='post_create'), # URL para criar um novo post
 path('<int:pk>/', PostDetailView.as_view(),
name='post_detail'), # URL para ver os detalhes de um post
 path('<int:pk>/update/', PostUpdateView.as_view(),
name='post_update'), # URL para atualizar um post existente
 path('<int:pk>/delete/', PostDeleteView.as_view(),
name='post_delete'), # URL para excluir um post existente
]