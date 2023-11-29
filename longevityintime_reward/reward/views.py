from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, TemplateView
from reward.forms import RegisterUserForm, LoginUserForm, AddWalletForm, AddTestCardForm
from reward.models import Wallet, TestCard
from reward.utils import DataMixin, menu
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
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


class AddWallet(LoginRequiredMixin, DataMixin, CreateView):
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

        # Сохраняем форму для получения экземпляра TestCard
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()

        # Получаем объект Wallet для текущего пользователя
        wallet = Wallet.objects.get(user=self.request.user)

        # Обновляем wallet_balance пользователя
        wallet.wallet_balance += 1
        wallet.save()

        return redirect(self.success_url)


class ProfilePage(LoginRequiredMixin, DataMixin, DetailView):
    model = Wallet
    template_name = 'rewards/profile.html'
    context_object_name = 'wallet'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="User Profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        return Wallet.objects.get(user=self.request.user)

# def addwallet(request):
#    if request.method == 'POST':
#        form = AddWalletForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('index')
#    else:
#        form = AddWalletForm()
#    return render(request, 'rewards/addwallet.html', {'form': form, 'menu': menu, 'title': 'Add Wallet'})


def profile(request):
    return HttpResponse("Profile Page")


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
        return reverse_lazy('profile')


def logout_user(request):
    logout(request)
    return redirect('login')
