from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

# The urlpatterns below matches the url requested to its corresponding views and templates.
# These urls handle all requests related to posts (CRUD).
# Plus a url path to the about page.

urlpatterns = [
    path('', PostListView.as_view(), name='projectunit-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='projectunit-about'),
]
