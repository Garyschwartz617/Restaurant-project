from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class TipeListView(LoginRequiredMixin,ListView):
    model = Tipe
    template_name = 'finance/all_tipes.html'

class TipeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Tipe
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('all_tipes') 
    def test_func(self):
        return self.request.user.is_superuser


class BillListView(LoginRequiredMixin,ListView):
    model = Bill
    template_name = 'finance/all_bills.html'


class BillDetailView(LoginRequiredMixin,DetailView):
    model = Bill
    template_name = 'finance/this_bill.html' 

class UpdateBillView(LoginRequiredMixin,UpdateView):
    model = Bill
    template_name = 'users/bill.html'
    success_url = reverse_lazy('home')


class BillDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Bill
    template_name = 'finance/delete_bill.html'
    success_url = reverse_lazy('all_bills') 
    def test_func(self):
        return self.request.user.is_superuser

