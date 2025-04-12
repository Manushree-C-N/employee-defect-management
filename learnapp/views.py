from django.shortcuts import render
from learnapp.forms import UserProfileForm, UserForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from DefectsPortal.models import Defect

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
    total_defects = Defect.objects.all()
    
    total_assigned = 0
    total_complete = 0
    pending_defects = 0
    total_primary = 0
    total_secondary = 0
    for i in total_defects:
        
        if request.user.username == i.assigned_to:
            total_assigned +=1
            if i.defect_status == 'COMPLETED':
                total_complete +=1
            elif i.defect_status == 'NOT COMPLETED':
                pending_defects +=1 
        
        if request.user.username == i.assigned_to:
            
            if i.defect_type == 'PRIMARY':
                total_primary += 8000
            elif i.defect_type == 'SECONDARY':
                total_secondary += 4000
    print(total_primary,total_secondary)


    context = {
        'total_complete': total_complete,
        'total_assigned': total_assigned,
        'pending_defects': pending_defects,
        'total_primary': total_primary,
        'total_secondary': total_secondary
    }

    return render(request,'dashboard.html',context)

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
