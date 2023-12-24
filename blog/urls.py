from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('about/', views.about, name="blog-about"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('future/', views.future, name="future"),
    path('home/', views.home, name="home"),
    path('deleted/', views.deleted, name="deleted"),
]
