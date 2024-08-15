from django.shortcuts import render
from . forms import ContactForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect

# Create your views here.
def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            return render(request,'contact.html',{'form':form,'result':'sucess'})
        return render(request,'contact.html',{'form':form,'result':'fail'})
        
    return render(request,'contact.html')

def login_view(request):
    return render(request,'login.html')


def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST )
        if form.is_valid():
            customer=form.save()
            login(request.customer.user)
            return redirect('customer:login')  
        
    return render(request,'register.html',{'form':form})
