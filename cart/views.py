from django.shortcuts import render
from online_shopping.models import product,cart

# Create your views here.
def finalcart(request):
    product_ids = []
    User_cart = cart.objects.filter(user_id=request.user.id)
    for prod in User_cart:
        product_ids.append(prod.prd_id_id)
        #print(prod.prd_id)
    print('product list:',product_ids)
    #product_ids = list(User_cart.objects.all().values_list('prd_id', flat=True))
    result = product.objects.filter(id__in = product_ids)
    return render(request,'Modified_files/cart.html',{'result':result})

def invoice(request):
    return render(request,'Modified_files/invoice.html')