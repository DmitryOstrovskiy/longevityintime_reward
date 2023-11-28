from django.urls import path
from reward.views import HomePageView, AboutPageView, add_wallet, add_test_card, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('add_wallet/', add_wallet, name='add_wallet'),
    path('add_test_card/', add_test_card, name='add_test_card'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]
