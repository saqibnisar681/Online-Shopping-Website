from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('xyz/<int:id>',views.xyz,name='xyz'),
    path('list_prd/<str:prod>',views.list_prd,name='list_prd'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)