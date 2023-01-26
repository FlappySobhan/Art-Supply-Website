from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Category

class ProductsView(ListView):
    model = Item
    template_name = "products/products-list.html"
    context_object_name = "products"
    paginate_by = 6
    paginate_orphans = 2

    def get_queryset(self):
        query = {}
        query['category__category_name__iexact']= self.request.GET.get('category', False)
        query['discount__gt']= self.request.GET.get('discount', False)
        self.mykwargs = {}
        for key, value in query.items():
            if value:
                self.mykwargs[key] = value
        try:
            return super().get_queryset().filter(**self.mykwargs)
        except:
            return super().get_queryset()

    def get_context_data(self, **mykwargs):
        context = super().get_context_data(**mykwargs)
        context['categories'] = Category.objects.filter(sub_category__isnull=True)
        for key, value in self.mykwargs.items():
            context[key.split('_')[0]] = value
        return context

class ProductView(DetailView):
    model = Item
    template_name = "products/products-detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_in_wishlist'] = self.request.user.profile.wishlist.filter(pk=self.object.pk).exists()
        return context

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user.profile.wishlist.filter(pk=object.pk).exists():
                self.request.user.profile.wishlist.remove(object)
            else:
                self.request.user.profile.wishlist.add(object)
            self.request.user.profile.save()
        return self.get(request, *args, **kwargs)