from kitchen.models import Course
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

# def cards(request):
#     return render(request,'card/cards.html', {'cards': Card.objects.all()})

def placeorder(request, pk):
    Cart.check_out(request,pk)
    if request.user.is_staff:
        return redirect (reverse('staff_order'))
    return redirect (reverse('cart'))



class CreateDishView(LoginRequiredMixin,CreateView):
    # model = Dish
    # fields = '__all__'
    # fields =['name', 'description','price', 'measurement','course']
    form_class = DishForm
    success_url = reverse_lazy('dish')
    template_name = 'service/dish.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishs'] = Dish.objects.all()
        form2 = CreateSingularForm(instance=self.request.user)
        context['form2'] = form2
        context['courses'] = Course.objects.all()

        return context

    def form_valid(self, form):
        dish = form.save(commit=False)
        dish.save()
        form.save_m2m()
        dish.cost = dish.get_cost()
        dish.save()
        return super().form_valid(form)


class DishDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Dish
    template_name = 'service/delete_dish.html'
    success_url = reverse_lazy('dish') 
    def test_func(self):
        return self.request.user.is_superuser


class MenuListView(ListView):
    model = Dish
    template_name = 'service/menu.html' 


class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'service/cart.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_cart'] = Cart.objects.filter(profile = self.request.user.profile)
        return context


class CreateSingularView(LoginRequiredMixin,CreateView):
    model = Singular
    fields =['comments']
    success_url = reverse_lazy('dish')
    template_name = 'service/singular.html'
   

    def form_valid(self, form):
        c = Cart.objects.filter(profile = self.request.user.profile).last()
        if  c.status == 'O':
            sing = form.save(commit=False)
            sing.cart = self.request.user.profile.cart_profile.last()
            sing.dish = Dish.objects.get(id = self.kwargs['pk'])
            sing.save()
            return super().form_valid(form)
        else:
            Cart.objects.create(profile = self.request.user.profile)
            sing = form.save(commit=False)
            sing.cart = self.request.user.profile.cart_profile.last()
            sing.dish = Dish.objects.get(id = self.kwargs['pk'])
            sing.save()
            return super().form_valid(form)

class UpdateSingular(LoginRequiredMixin,UpdateView):
    model = Singular
    fields =['comments']
    template_name = 'service/update_singular.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            singular = Singular.objects.get(id = self.kwargs['pk'])
            crt = singular.cart.id
            return reverse_lazy('staff_singular', kwargs= {'pk': crt })
        else:
            return reverse_lazy('cart')


class SingularDeleteView(LoginRequiredMixin,DeleteView):
    model = Singular
    template_name = 'service/delete_singular.html'
    success_url = reverse_lazy('cart') 
    
    # def get_success_url(self):
    #     if self.request.user.is_staff:
    #         singular = Singular.objects.get(id = self.kwargs['pk'])
    #         crt = singular.cart.id
    #         return reverse_lazy('staff_singular', kwargs= {'pk': crt })
    #     else:
    #         return reverse_lazy('cart')


class CreateStaffOrderView(LoginRequiredMixin,CreateView):
    model = Cart
    fields =['customer']
    success_url = reverse_lazy('staff_order')
    template_name = 'service/staff_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all().order_by('-date_created')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user.profile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CartDeleteView(LoginRequiredMixin,DeleteView):
    model = Cart
    template_name = 'service/delete_cart.html'
    success_url = reverse_lazy('staff_order') 


class CreateStaffSingularView(LoginRequiredMixin,CreateView):
    model = Singular
    fields =['comments']
    template_name = 'service/staff_singular.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishs'] = Dish.objects.all()
        context['cart'] = Cart.objects.get(id = self.kwargs['pk'])
        context['singulars'] = Singular.objects.filter(cart = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        sing = form.save(commit=False)
        sing.cart = Cart.objects.get(id = self.kwargs['pk'])
        sing.dish = Dish.objects.get(id = self.kwargs['dish_pk'])
        sing.save()
        return super().form_valid(form)
    
    def get_success_url(self):

        return reverse_lazy('staff_singular', kwargs= {'pk': self.kwargs['pk'] })

class StaffSingularDeleteView(LoginRequiredMixin,DeleteView):
    model = Singular
    template_name = 'service/delete_singular.html'
    success_url = reverse_lazy('staff_order') 


