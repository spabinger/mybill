from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required

from mybill.forms import BillFormSimple, BillFormComplex
from .models import Bill, Store, StoreBrand, StoreType
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



def about(request):
    return render(request, 'mybill/about.html')


@login_required
def home(request):
    return render(request, 'mybill/home.html')


@login_required
def add_bill_simple(request):
    if request.method == 'POST':
        form = BillFormSimple(request.POST, request.FILES)
        if form.is_valid():
            bill = form.save(commit=False)

            ## TODO Parse image

            ## These entries will be filled later
            bill.amount = 1.0
            bill.date = "2010-01-01"
            bill.store = Store.objects.all()[0]


            bill.created_by = request.user

            bill.save()

            return redirect('bills', pk=bill.pk)  # TODO: redirect to the created topic page
    else:
        form = BillFormSimple()

    return render(request, 'mybill/add_bill_simple.html', {'form': form})


@login_required
def add_bill_complex(request):
    if request.method == 'POST':
        form = BillFormComplex(request.POST, request.FILES)
        if form.is_valid():
            bill = form.save(commit=False)

            bill.created_by = request.user

            bill.save()

            return redirect('bills', pk=bill.pk)  # TODO: redirect to the created topic page
    else:
        form = BillFormComplex()

    return render(request, 'mybill/add_bill_complex.html', {'form': form})


class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    context_object_name = 'bills'
    template_name = 'mybill/list_bills.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['bill'] = self.bill
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        #self.bill = get_object_or_404(Bill, pk=self.kwargs.get('pk'))
        self.bill = Bill.objects.all()
        return self.bill


class BillDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    template_name = 'mybill/view_bill.html'

    #def get_context_data(self, **kwargs):
    #    context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context




class StoreAddView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['name', 'brand']
    #form_class = StoreForm
    success_url = reverse_lazy('stores')
    template_name = 'mybill/new_model_template.html'

class StoreDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    template_name = 'mybill/view_store.html'


class StoreListView(LoginRequiredMixin, ListView):
    model = Store
    template_name = 'mybill/list_template.html'


class StoreBrandAddView(LoginRequiredMixin, CreateView):
    model = StoreBrand
    fields = ['name', 'store_type']
    success_url = reverse_lazy('store_brands')
    template_name = 'mybill/new_model_template.html'


class StoreBrandListView(LoginRequiredMixin, ListView):
    model = StoreBrand
    template_name = 'mybill/list_template.html'


class StoreTypeAddView(LoginRequiredMixin, CreateView):
    model = StoreType
    fields = ['store_type']
    #form_class = StoreForm
    success_url = reverse_lazy('store_types')
    template_name = 'mybill/new_model_template.html'


class StoreTypeListView(LoginRequiredMixin, ListView):
    model = StoreType
    template_name = 'mybill/list_template.html'



