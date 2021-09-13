from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView,DeleteView,ListView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *
from service.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
# Create your views here.



def homepage(request):
    return render(request, 'users/homepage.html')

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def form_valid(self, form):
        new_user = form.save()
        new_user.refresh_from_db()
        profile_form = ProfileForm(self.request.POST, instance= new_user.profile)
        if profile_form.is_valid():
            new_user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user:
                login(self.request, user)
            return redirect('home')
        else:
            new_user.delete()
            return self.form_invalid(form)


class UpdateProfile(LoginRequiredMixin,UpdateView):
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditUserForm(instance=self.request.user)
        return context
    
    def get_object(self, queryset= None):
        return self.request.user.profile

    def form_valid(self, form):
        user_form = EditUserForm(self.request.POST, instance = self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

class UserListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = User
    template_name = 'users/all_users.html'
    def test_func(self):
        return self.request.user.is_superuser

class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('all_users') 
    def test_func(self):
        return self.request.user.is_superuser

class StaffRegisterCreationView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/staff_register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_unusable_password()
        new_user.save()
        new_user.refresh_from_db()
        profile_form = ProfileForm(self.request.POST, instance=new_user.profile)
        if profile_form.is_valid():
            print(form.cleaned_data)
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            return redirect('staff_order')
        else:
            new_user.delete()
            return self.form_invalid(form)


def start_cart(request):
    
    return render(request, 'users/start_cart.html')

def search_user(request):
    query = request.GET.get('search')
    print(request.GET)
    user =  User.objects.filter(
        Q(first_name__contains=query) |
        Q(last_name__contains=query)  |
        Q(email__contains=query)  |
        Q(username__contains=query)
    )
    profile =  Profile.objects.filter(
        Q(number__contains=query) |
        Q(address__contains=query)  
    )
 
    results = {
        
        'profiles': profile,
        'users': user
    }

    return render(request, 'users/search_user.html', {'q':query, 'results': results})


def create_cart(request, pk):
    pf = Profile.objects.get(id = pk)
    Cart.objects.create(profile =pf)
    return redirect (reverse('staff_order'))
