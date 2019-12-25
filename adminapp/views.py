# from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from mainapp.models import Product
from mainapp.models import ProductCategory

# Create your views here.


class IsUserAdminView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(IsUserAdminView, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({"title": 'Продукты',
                        'categories': ProductCategory.objects.all()})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_pk = self.kwargs.get('cat_pk')
        if category_pk:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            # print(category)
            queryset = queryset.filter(category=category)
            # print(queryset)
        return queryset


class ProductDetailView(IsUserAdminView, DetailView):
    model = Product
    template_name = 'adminapp/detailed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.object.name})
        # p = get_object_or_404(Product, pk=self.kwargs['product_pk'])
        # print(f' продукт - {p}')
        # print(f' keys - {context.keys()}')
        return context


class ProductCreateView(IsUserAdminView, CreateView):
    model = Product
    template_name = 'adminapp/update.html'
    fields = '__all__'
    # success_url = reverse_lazy('adminapp:product')

    def get_success_url(self):
        return reverse_lazy('adminapp:detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(IsUserAdminView, UpdateView):
    model = Product
    template_name = 'adminapp/update.html'
    fields = '__all__'
    # success_url = reverse_lazy('adminapp:product')

    def get_success_url(self):
        return reverse_lazy('adminapp:detail', kwargs={'pk': self.kwargs.get("pk")})


class ProductDeleteView(IsUserAdminView, DeleteView):
    model = Product
    template_name = 'adminapp/delete_alarm.html'
    success_url = reverse_lazy('adminapp:product')
