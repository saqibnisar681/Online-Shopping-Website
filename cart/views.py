from django.shortcuts import render,redirect
from online_shopping.models import product,cart
from django.urls import reverse
from django.http import HttpResponseRedirect

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

def dele(request,id):
    c = product.objects.get(pk=id)
    data = cart.objects.filter(prd_id = c,user_id = request.user.id).delete()
    # return redirect(reverse('cart:finalcart'))
    return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
    # c = cart.objects.get(pk=id)
    # data = cart.objects.create(prd_id = c,user_id = request.user.id) delete
    # return redirect(data)

def index(request):
    return redirect('/')