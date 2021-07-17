from os import name
from django.contrib.auth.models import User
from main.models import Place
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
# prevent users to access any page without login
from django.contrib.auth.mixins import LoginRequiredMixin
# use an django built in user creation form
from django.contrib.auth.forms import UserCreationForm
# for that user who already logged in
from django.contrib.auth import login
# search by different queries
from django.db.models import Q

from .models import Place

class UserRegister(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('places')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('places')
        return super(UserRegister, self).get(*args, **kwargs)

class UserLogin(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('places')

class PlaceList(LoginRequiredMixin, ListView):
    model = Place
    context_object_name = 'places' #object_list is named as places

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places'] = context['places'].filter(user=self.request.user)
        context['count'] = context['places'].filter(visited=False).count()
        # logic for search
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['places'] = context['places'].filter(
                Q(name__startswith=search_input)|
                Q(country__startswith = search_input))
        context['search_input'] = search_input
        return context

class PlaceDetail(LoginRequiredMixin, DetailView):
    model = Place
    context_object_name = 'details'

class PlaceCreate(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['name', 'country', 'image', 'description', 'visited'] #can set all together '__all__'
    success_url = reverse_lazy('places')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaceCreate, self).form_valid(form)

class PlaceUpdate(LoginRequiredMixin, UpdateView):
    model = Place
    context_object_name = 'details'
    fields = ['name', 'country', 'image', 'description', 'visited']
    success_url = reverse_lazy('places')

class PlaceDelete(LoginRequiredMixin, DeleteView):
    model = Place
    context_object_name = 'details'
    success_url = reverse_lazy('places')