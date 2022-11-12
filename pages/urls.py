from django.urls import path
from .views import AboutPageView, HomePageView, RegisterPageView, BlockPageView, BlockchainPageView, homePageView, get_user

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('register', RegisterPageView.as_view(), name='register'),
    path('block/', BlockPageView.as_view(), name='block'),
    path('blockchain/', BlockchainPageView.as_view(), name='blockchain'),
    path('', HomePageView.as_view(), name='home'),
]
