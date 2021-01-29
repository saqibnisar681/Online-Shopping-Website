from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart',views.finalcart,name='finalcart'),
    path('cart/invoice',views.invoice,name='invoice'),
]
