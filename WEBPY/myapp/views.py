from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.contrib.auth.models import User
from .models import Category,Product, User as Uc
from .models import  User as Uc
from .forms import CreateNewProduct,RegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def register ( request ) :
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            Uc.objects.create(
                username=request.POST["username"],
                email=request.POST["email"],
                age=request.POST["age"],
                address=request.POST["address"],
                image=request.POST["image"],
                )
            form.save()
            messages.success ( request ,'Welcome { username }, your account is activated')
            return redirect ('about.html')
    else :
        form = RegisterForm()
    return render (request ,'users/register.html',{'form' :form} )



def index(request):
    title = 'Welcome Django'
    return render(request, 'index.html', {
        'title': title
    })

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def products(request):
    # task=get_object_or_404(Task.objects.get(id=id))
    products = Product.objects.all()
    return render(request, 'products/products.html', {
        'products': products
    })  

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateNewProduct(request.POST)
        if form.is_valid():
            form = form.save()
            # Product.objects.create(code=request.POST['code'],
            #                         name=request.POST['name'],
            #                         description=request.POST['description'],
            #                         price_unit=request.POST['price_unit'],
            #                         quantity=request.POST['quantity'],
            #                         type_product=request.POST['type_product'],
            #                         category=request.POST['category'],
            #                         )
            messages.success(request ,'Producto agregado')
            return redirect('products')
    else :
        form = CreateNewProduct()
    return render (request ,'products/create_products.html',{'form' :form} )

   

