from django.urls import path
from reward.views import HomePageView, AboutPageView, AddWallet, ProfilePage, AddTestCard, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('add_wallet/', AddWallet.as_view(), name='add_wallet'),
    path('add_test_card/', AddTestCard.as_view(), name='add_test_card'),
    path('profile/', ProfilePage.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]
