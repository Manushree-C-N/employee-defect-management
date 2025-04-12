
from django.shortcuts import render, redirect
from DefectsPortal.models import Defect, Defects_screen_shots
from DefectsPortal.forms import AddDefectForm, Defect_Edit_Form
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url='login')
def defect(request):
    defects = Defect.objects.all()
    total_defects = len(defects)
    paginator = Paginator(defects, 4)
    page = request.GET.get('pg')
    defects = paginator.get_page(page)

    contexts = {
        'defects': defects,
        'total_defects': total_defects
    }
    return render(request, 'defects/defect.html', {'contexts': contexts})

@login_required(login_url='login')
def defect_description(request, id=0):
    defe = Defect.objects.get(id=id)
    images = Defects_screen_shots.objects.filter(defect=defe)
    context = {
        'defe': defe,
        'images': images
    }
    return render(request, 'defects/description.html', {'context': context})

@login_required(login_url='login')
def add_defect(request):
    items = AddDefectForm()
    if request.method == 'POST':
        items = AddDefectForm(request.POST)
        if items.is_valid():
            items.save()
            return redirect('defect')
    return render(request, 'defects/add_defects.html', {'items': items})

@login_required(login_url='login')
def update_defects(request, id=0):
  
    defect = Defect.objects.get(id=id)
    form = Defect_Edit_Form(instance=defect)
    if request.method == 'POST':
        form = Defect_Edit_Form(request.POST, instance=defect)
        if form.is_valid():
            form.save()
            return redirect('defect')
    return render(request, 'defects/edit_defects.html', {'form': form})

@login_required(login_url='login')
def delete_defects(request, id=0):
    defect = Defect.objects.get(id=id)
    defect.delete()
    return redirect('defect')