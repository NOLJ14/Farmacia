from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
	path('image', producto_image_view, name = 'image_upload'), 
	path('success', success, name = 'success'), 
    path('product_images', display_product_images, name = 'product_images'),
] 

if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 
