from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from reward.forms import RegisterUserForm, LoginUserForm
from reward.utils import DataMixin, menu
# from .models import Reward


# def reward_list(request):
#    rewards = Reward.objects.filter(user=request.user)
#    return render(request, 'rewards/reward_list.html', {'rewards': rewards})

# menu = [{'title': "Add wallet", 'url_name': 'add_wallet'},
#        {'title': "Add a test card", 'url_name': 'add_test_card'},
#        {'title': "About", 'url_name': 'about'},]


# def index(request):
#    context = {
#        'menu': menu,
#        'title': 'Main page'}
#   return render(request, 'rewards/index.html', context=context)


class HomePageView(DataMixin, TemplateView):
    template_name = "rewards/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home Page")
        return dict(list(context.items()) + list(c_def.items()))


class AboutPageView(DataMixin, TemplateView):
    template_name = "rewards/about.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About")
        return dict(list(context.items()) + list(c_def.items()))

# def about(request):
#    context = {
#        'menu': menu,
#        'title': 'About'}
#    return render(request, 'rewards/about.html', context=context)


def add_wallet(request):
    return HttpResponse("Add Wallet")


def add_test_card(request):
    return HttpResponse("Add test Card")


# def login(request):
#    return HttpResponse("Authorization")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'rewards/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'rewards/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
