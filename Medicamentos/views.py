from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
#from .models import Producto

# Create your views here. 
def producto_image_view(request): 

	if request.method == 'POST': 
		form = ProductoForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success') 
	else: 
		form = ProductoForm() 
	return render(request, 'Medicamentos/ProductosFormulario.html', {'form' : form}) 

def index(request):
    return HttpResponse('successfully uploaded') 

def success(request): 
	return HttpResponse('successfully uploaded') 

# Python program to view 
# for displaying images 

def display_product_images(request): 

	if request.method == 'GET': 

		# getting all the objects of hotel. 
		Products = Producto.objects.all() 
		return render(request, 'Medicamentos/display_product_images.html', 
					{'product_images' : Products}) 


