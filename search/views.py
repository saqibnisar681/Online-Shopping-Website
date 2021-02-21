from django.shortcuts import render, redirect
from online_shopping.models import product,cart
from django.db.models import Q


# Create your views here.
def searchalgo(request):
    queru = None
    results = []
    if request.method == "GET":
        query = request.GET.get('s')
        results = product.objects.filter( Q(name__icontains=query) )
        return render(request, 'Modified_files/product.html', {'results': results})

def index(request):
    return redirect('/')
