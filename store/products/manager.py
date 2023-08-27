from core.managers import BaseManager

class ItemManager(BaseManager):
    def is_available(self):
        return super().get_queryset().filter(stock__gt=0)
    
    def is_not_available(self):
        return super().get_queryset().filter(stock__lte=0)

    def is_discounted(self):
        return super().get_queryset().filter(stock__gt=0, discount__gt=0).order_by('-discount')
    
    def last_items(self, number, **kwargs):
        return super().get_queryset().filter(**kwargs).order_by('-created_at')[:number]
