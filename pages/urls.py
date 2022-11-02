from django.urls import path
from .views import AboutPageView, HomePageView, homePageView, get_user

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]