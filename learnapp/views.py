from django.shortcuts import render
from learnapp.forms import UserProfileForm, UserForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    registered = False
    
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)    
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form1 = UserForm()
        form2 = UserProfileForm()

    context = {
        'form1': form1,
        'form2': form2,
        'registered': registered
    }
    return render(request, 'registeration.html', context)

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #authentication step
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("Please Check your creds...!!!")
    return render(request,"login.html")


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login')
def userEdit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserEditForm(instance=request.user)
    return render(request,'edit.html',{'form':form})
