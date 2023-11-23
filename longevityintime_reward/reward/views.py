from django.shortcuts import render
from .models import Reward


def reward_list(request):
    rewards = Reward.objects.filter(user=request.user)
    return render(request, 'rewards/reward_list.html', {'rewards': rewards})
