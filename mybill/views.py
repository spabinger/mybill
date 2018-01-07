from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required

from mybill.forms import BillForm
from .models import Bill, Store, StoreBrand, StoreType
from django.urls import reverse_lazy




def about(request):
    return render(request, 'mybill/about.html')


@login_required
def home(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)

            bill.created_by = request.user

            bill.save()

            #topic.board = board
            #topic.starter = user
            #topic.save()
            #post = Post.objects.create(
            #    message=form.cleaned_data.get('message'),
            #    topic=topic,
            #    created_by=user
            #)
            return redirect('bills', pk=bill.pk)  # TODO: redirect to the created topic page
    else:
        form = BillForm()

    return render(request, 'mybill/home.html', {'form': form})





class BillListView(ListView):
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


class BillDetailView(DetailView):

    model = Bill

    template_name = 'mybill/view_bill.html'

    #def get_context_data(self, **kwargs):
    #    context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context




class StoreAddView(CreateView):
    model = Store
    fields = ['name', 'brand']
    #form_class = StoreForm
    success_url = reverse_lazy('stores')
    template_name = 'mybill/new_model_template.html'


class StoreListView(ListView):
    model = Store
    template_name = 'mybill/list_template.html'


class StoreBrandAddView(CreateView):
    model = StoreBrand
    fields = ['name', 'store_type']
    success_url = reverse_lazy('store_brands')
    template_name = 'mybill/new_model_template.html'


class StoreBrandListView(ListView):
    model = StoreBrand
    template_name = 'mybill/list_template.html'


class StoreTypeAddView(CreateView):
    model = StoreType
    fields = ['store_type']
    #form_class = StoreForm
    success_url = reverse_lazy('store_types')
    template_name = 'mybill/new_model_template.html'


class StoreTypeListView(ListView):
    model = StoreType
    template_name = 'mybill/list_template.html'



