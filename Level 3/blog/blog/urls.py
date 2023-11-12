from django.urls import path
from .views import (
    HomePageView,
    PostDetailView,
    BlogCreateView,
    BlogDeleteView,
    BlogUpdateView
)

urlpatterns = [
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'), # new
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('',HomePageView.as_view(),name = 'home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'), # new
]