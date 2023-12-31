from django.shortcuts import render , redirect
from .forms import SignupForm , ActivationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

from .models import Profile



from products.models import Product , Brand , Review
from orders.models import Order



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            user = form.save(commit=False)
            user.is_active = False
            
            form.save()
            
            # profile --> code
            profile = Profile.objects.get(user__username=username)
            
            # send email 
            send_mail(
                "Activate Your Account",
                f"Welcome {username} \nuse this code {profile.code} to activate your account",
                "rawit6867@gmail.com",
                [email],
                fail_silently=False,
            )
            
            return redirect(f'/accounts/{username}/activate')
        
    else:
        form = SignupForm()
        
    return render(request,'registration/signup.html',{'form':form})



def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                
                user = User.objects.get(username=profile.user.username)
                user.is_active = True
                user.save()                
                profile.save()
                
                return redirect('/accounts/login')
        
        
    else:
        form = ActivationForm()
        
    return render(request,'registration/activate.html',{'form':form})



@login_required
def dashboard(request):
    new_products = Product.objects.filter(flag='New').count()
    sale_products = Product.objects.filter(flag='Sale').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    
    users = User.objects.all().count()
    orders = Order.objects.all().count()
    products = Product.objects.all().count()
    brand = Brand.objects.all().count()
    reviews = Review.objects.all().count()
    
    return render(request,'accounts/dashboard.html',{
        'new_products': new_products , 
        'sale_products': sale_products , 
        'feature_products': feature_products , 
        
        'users': users , 
        'orders': orders , 
        'products': products , 
        'brand': brand , 
        'reviews': reviews
    })
