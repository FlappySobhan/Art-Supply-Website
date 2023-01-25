from .models import Category

def categories(request):
    categories = Category.objects.filter(sub_category=None)
    return {'categories': categories}