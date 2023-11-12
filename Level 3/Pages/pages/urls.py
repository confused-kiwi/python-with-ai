from .views import HomePageView, AboutPageView
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about')
]
