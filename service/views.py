from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
# Create your views here.

# def cards(request):
#     return render(request,'card/cards.html', {'cards': Card.objects.all()})

def placeorder(request, pk):
    Cart.check_out(request,pk)
    return redirect (reverse('cart'))



class CreateDishView(LoginRequiredMixin,CreateView):
    model = Dish
    # fields = '__all__'
    fields =['name', 'description','price', 'measurement']
    success_url = reverse_lazy('dish')
    template_name = 'service/dish.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishs'] = Dish.objects.all()
        form2 = CreateSingularForm(instance=self.request.user)
        context['form2'] = form2

        return context

    def form_valid(self, form):
        dish = form.save(commit=False)
        dish.save()
        form.save_m2m()
        dish.cost = dish.get_cost()
        dish.save()
        return super().form_valid(form)


# class DishListView(ListView):
#     model = Dish
#     template_name = 'service/all_dishs.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = CreateSingularForm(instance=self.request.user)
#         context['form'] = form
#         return context


class DishDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Dish
    template_name = 'service/delete_dish.html'
    success_url = reverse_lazy('dish') 
    def test_func(self):
        return self.request.user.is_superuser


class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'service/cart.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EditSingularForm(instance=self.request.user)
        form.fields['cart'].queryset = Cart.objects.filter(profile = self.request.user.profile)
        context['form'] = form
        context['my_cart'] = Cart.objects.filter(profile = self.request.user.profile)
        return context


class CreateSingularView(LoginRequiredMixin,CreateView):
    model = Singular
    fields =['comments']
    success_url = reverse_lazy('dish')
    template_name = 'service/singular.html'
   

    def form_valid(self, form):
        sing = form.save(commit=False)
        sing.cart = self.request.user.profile.cart_set.last()
        sing.dish = Dish.objects.get(id = self.kwargs['pk'])
        sing.save()
        return super().form_valid(form)


class SingularDeleteView(LoginRequiredMixin,DeleteView):
    model = Singular
    template_name = 'service/delete_singular.html'
    success_url = reverse_lazy('cart') 

