from django.urls import path
from .views import reward_list

urlpatterns = [
    path('rewards/', reward_list, name='reward_list'),
]
