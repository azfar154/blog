from django.urls import path,include
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView
urlpatterns=[
    path('',PostListView.as_view(),name="about-page"),
    path('data/',views.data,name="data-page"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-page"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="post-update"),
    ]
    