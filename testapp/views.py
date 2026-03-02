from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyView(ListView):
    model = Company
    
    #default template file :modelname_list.html
    #default context object name :modelname_list  
    
class ComapnyDetails(DetailView):  
    model = Company
    
    #default template file :modelname_detail.html
    #default context object name :modelname or object
    
class CompanyCreate(CreateView):
    model = Company
    fields = "__all__"
    #default template file : modelname_form.html
    
class CompanyUpdate(UpdateView):
    model = Company
    fields = ('location','ceo')
    
class CompanyDelete(DeleteView):
    model = Company
    success_url=reverse_lazy('clist')