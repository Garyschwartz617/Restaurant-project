from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def kitchen(request):
    return render(request, 'kitchen/kitchen.html')


class CreateIngrediantView(LoginRequiredMixin,CreateView):
    model = Ingrediant
    fields ='__all__'
    success_url = reverse_lazy('all_ingrediants',)
    template_name = 'kitchen/all_ingrediants.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingrediants'] = Ingrediant.objects.all()
        return context


class IngrediantDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Ingrediant
    template_name = 'kitchen/delete_ingrediant.html'
    success_url = reverse_lazy('all_ingrediants') 
    def test_func(self):
        return self.request.user.is_superuser


class CreateMeasurementView(LoginRequiredMixin,CreateView):
    model = Measurement
    fields ='__all__'
    success_url = reverse_lazy('all_measurements',)
    template_name = 'kitchen/all_measurements.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['measurements'] = Measurement.objects.all()
        return context


class MeasurementDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Measurement
    template_name = 'kitchen/delete_measurement.html'
    success_url = reverse_lazy('all_measurements') 
    def test_func(self):
        return self.request.user.is_superuser


class CreateTransactionView(LoginRequiredMixin,CreateView):
    model = Transaction
    fields ='__all__'
    success_url = reverse_lazy('all_transactions',)
    template_name = 'kitchen/all_transactions.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        return context


class CreateComboView(LoginRequiredMixin,CreateView):
    model = Combo
    fields =['measurement', 'ingrediant']
    success_url = reverse_lazy('all_combos',)
    template_name = 'kitchen/all_combos.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['combos'] = Combo.objects.all()
        return context
    
    def form_valid(self, form):
        combo = form.save(commit=False)
        c =combo.cost_per()
        combo.cost = c
        combo.save()
        return super().form_valid(form)


class ComboDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Combo
    template_name = 'kitchen/delete_combo.html'
    success_url = reverse_lazy('all_combos') 
    def test_func(self):
        return self.request.user.is_superuser
