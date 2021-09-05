from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class CreateTipesView(LoginRequiredMixin,CreateView):
    model = Tipe
    fields ='__all__'
    success_url = reverse_lazy('all_tipes',)
    template_name = 'finance/all_tipes.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipes'] = Tipe.objects.all()
        return context


class TipeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Tipe
    template_name = 'finance/delete_user.html'
    success_url = reverse_lazy('all_tipes') 
    def test_func(self):
        return self.request.user.is_superuser


class CreateBillView(LoginRequiredMixin,CreateView):
    model = Bill
    fields ='__all__'
    template_name = 'finance/all_bills.html'
    success_url = reverse_lazy('all_bills',)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bills'] = Bill.objects.all()
        return context


class BillDetailView(LoginRequiredMixin,DetailView):
    model = Bill
    template_name = 'finance/bill.html' 


class UpdateBillView(LoginRequiredMixin,UpdateView):
    model = Bill
    fields ='__all__'

    template_name = 'finance/edit_bill.html'
    success_url = reverse_lazy('all_bills')


class BillDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Bill
    template_name = 'finance/delete_bill.html'
    success_url = reverse_lazy('all_bills') 
    def test_func(self):
        return self.request.user.is_superuser

