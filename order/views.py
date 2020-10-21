import json

from django.views     import View
from django.db.models import Prefetch
from django.http      import (
    JsonResponse,
    HttpResponse
)

from .models        import Cart
from user.utils     import login_required
from user.models    import User
from product.models import (
    Product,
    Image
)

class CartView(View):
    @login_required
    def post(self, request):
        try:
            data      = json.loads(request.body)

            if not Cart.objects.filter(user_id = request.user.id, product_id = data['product_id']).exists():
                Cart.objects.create(
                    user        = request.user,
                    product     = Product.objects.get(id = data['product_id']),
                    total_price = data['total_price'],
                )
                return JsonResponse({'message' : 'CART ADDED'}, status = 201)

            return JsonResponse({'message' : 'ALREADY EXIST PRODUCT' }, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY ERROR'}, status = 400)            
    
    @login_required
    def get(self, request):
        try:
            user      = request.user

            items     = Cart.objects.filter(user_id = request.user.id)
            cart_list = [{
                "ID"       : item.product.id,
                'quantity' : item.quantity,
                'name'     : item.product.name,
                'price'    : item.product.price,
                'image_url': item.product.image_set.first().image_url
            } for item in items]
            return JsonResponse({'cart_list' : cart_list}, status = 200)
    
        except KeyError:
            return JsonResponse({'message' : 'KEY ERROR'}, status = 400)

    @login_required
    def delete(self, request):
        data = json.loads(request.body)
        try:
            user = request.user
            item = Cart.objects.get(user_id = request.user.id, product_id = data['product_id'])
            item.delete()
            return JsonResponse({'message' : 'DELETED'}, status = 200)
        
        except  KeyError:
            return JsonResponse({'message' : 'KEY ERROR'}, status = 400)

    @login_required
    def patch(self, request):
        data = json.loads(request.body)
        try:
            user = request.user
            item = Cart.objects.get(user_id = request.user.id, product_id = data['product_id'])
            if data['changed_quantity'] == 'plus':
                item.quantity +=1
                item.save()
                return HttpResponse(status = 200)

            data['changed_quantity'] == 'minus'
            item.quantity -=1
            item.save()
            return HttpResponse(status = 200)
                
        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)