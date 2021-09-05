from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# def cards(request):
#     return render(request,'card/cards.html', {'cards': Card.objects.all()})

class CreateDishView(LoginRequiredMixin,CreateView):
    model = Dish
    # fields = '__all__'
    fields =['name', 'description','price', 'measurement']
    success_url = reverse_lazy('dish')
    template_name = 'service/dish.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishs'] = Dish.objects.all()
        return context
    def get_form(self, form_class= None):
        form = super().get_form(form_class=form_class)
        # form.cost = form.fields['measurement'].queryset.get_cost()
        return form

    def form_valid(self, form):
        dish = form.save(commit=False)
        # print('HELLO')
        # print(dish)
        # ingrediants = dish.measurement
        # print(ingrediants)
        # cost = 0
        # for ingrediant in ingrediants:
        #     print(ingrediant)
        #     cost += ingrediant.cost

        # dish.cost = dish.get_cost()
        dish.save()
        print(dish.name)
        print(dish.price)
        print(dish.measurement)
        d = dish.measurement.all()
        for a in d:
            print('hey')
            print(a)
        # print(dish.fields['measurement'].queryset)
        # dish.cost = dish.get_cost()
        # dish.save()
        return super().form_valid(form)



class DishDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Dish
    template_name = 'service/delete_dish.html'
    success_url = reverse_lazy('dish') 
    def test_func(self):
        return self.request.user.is_superuser
