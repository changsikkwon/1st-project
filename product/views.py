import json

from django.views           import View
from django.http            import JsonResponse
from django.db.models       import Prefetch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models       import Q

from .models                import(
    Category,
    Product,
    Image,
    HtmlTag,
)

class ProductsView(View):
    def menu(self, q):
        products = Product.objects.filter(q)
        return [
            {
                "ID"    : product.id,
                "name"  : product.name,
                "price" : product.price,
                "image" : product.image_set.first().image_url,
            } 
        for product in products]
    
    def get(self, request):
        word     = request.GET.get('search', None)
        pk       = request.GET.get('category', None)
        category = Category.objects.prefetch_related(Prefetch('product_set', queryset=Product.objects.prefetch_related('image_set')))

        if word:
            return JsonResponse({'data' : self.menu(Q (name__icontains = word) | Q (category__name__icontains = word))}, status = 200)
        elif pk:
            return JsonResponse({'data' : self.menu(Q (category__id__icontains = pk))}, status = 200)
        
        return JsonResponse({"message" : "ValueError"}, status = 400) 

class ProductView(View):
    def get(self, request, pk):
        if Product.objects.filter(pk = pk).exists():
            return JsonResponse({"html" : [Product.objects.get(pk = pk).htmltag.description]}, status = 200)
        return JsonResponse({"message" : "Product Does Not Exist"}, status = 400)