from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.basic, name="basic"),
    # path("",views.index,name="index"),
    # path(route='add/', view=views.cart_add, name="cart_add"),
    path('myproduct/', view=views.myproduct, name='myproduct'),
    path('addtocart/', view=views.addtocart, name='addtocart'),
    path('mycart/', view=views.mycart, name="mycart"),
    path('cartdelete/<int:id>/', view=views.cart_delete, name="cartdelete"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
