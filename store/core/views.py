from django.shortcuts import render

from django.views.generic import TemplateView
from products.models import Item

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_items'] = Item.objects.last_items(4, stock__gt=0)
        context['discounted_items'] = Item.objects.is_discounted()[:2]
        return context
