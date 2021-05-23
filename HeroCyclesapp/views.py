from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout ,authenticate
from .models import bicycles


def home(request):
    return render(request,'home.html')  

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('/')

    else:    
        return render(request,'login.html') 

def mountain(request):
    bicycle = bicycles.objects.all()
    return render(request,'mountain.html',{'bicycles':bicycle})

def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password and len(fname)<20 and len(lname)<20 and len(username)<20:
            user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
            user.save()
            return redirect('/')
        else:
            return redirect('/formvalidations')    
    else:
        return render(request,'signup.html')

def handlelogout(request):
    logout(request)
    return redirect('/')

def handlesearch(request):
    query = request.GET['searcher']
    bicycle = bicycles.objects.filter(name__icontains=query)
    return render(request,'mountain.html',{'bicycles':bicycle})

def formvalidations(request):
    return render(request,'formvalidations.html')
    