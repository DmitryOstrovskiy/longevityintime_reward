from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, TemplateView
from reward.forms import (RegisterUserForm, LoginUserForm, AddWalletForm,
                          AddTestCardForm)
from reward.models import Wallet
from reward.utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(DataMixin, TemplateView):
    '''A class for displaying the main page.
    A function for displaying the title and the page menu.'''
    template_name = "rewards/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home Page")
        return dict(list(context.items()) + list(c_def.items()))


class AboutPageView(DataMixin, TemplateView):
    '''A class for displaying the about page.
    A function for displaying the title and the page menu.'''
    template_name = "rewards/about.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About")
        return dict(list(context.items()) + list(c_def.items()))


class AddWallet(LoginRequiredMixin, DataMixin, CreateView):
    '''Class for adding Wallet model data'''
    form_class = AddWalletForm
    template_name = 'rewards/addwallet.html'
    success_url = reverse_lazy('profile')
    login_url = reverse_lazy('profile')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Wallet")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        wallet = Wallet.objects.filter(user=self.request.user).first()
        if wallet:
            return redirect('profile')

        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTestCard(LoginRequiredMixin, DataMixin, CreateView):
    '''Class for adding TestCard model data'''
    form_class = AddTestCardForm
    template_name = 'rewards/addtestcard.html'
    success_url = reverse_lazy('profile')
    login_url = reverse_lazy('profile')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add a Test Card")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Saving the form to get a TestCard instance
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()

        # Getting the Wallet object for the current user
        wallet = Wallet.objects.get(user=self.request.user)

        # Updating the user's wallet_balance
        wallet.wallet_balance += 1
        wallet.save()

        return redirect(self.success_url)


class ProfilePage(LoginRequiredMixin, DataMixin, DetailView):
    '''Class for displaying the user profile page'''
    model = Wallet
    template_name = 'rewards/profile.html'
    context_object_name = 'wallet'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="User Profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        return Wallet.objects.get(user=self.request.user)


class RegisterUser(DataMixin, CreateView):
    '''Class for user registration'''
    form_class = RegisterUserForm
    template_name = 'rewards/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    # The function of automatic login to the site,
    # after successful registration.
    # The user is immediately redirected to the profile page.
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(DataMixin, LoginView):
    '''The class to log in'''
    form_class = LoginUserForm
    template_name = 'rewards/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('profile')


# Function for logout and redirected to login page
def logout_user(request):
    logout(request)
    return redirect('login')
