from django.shortcuts import render, redirect
from DefectsPortal.models import Defect, Defects_screen_shots
from DefectsPortal.forms import AddDefectForm


# Create your views here.
def defect(request):

    defects = Defect.objects.all()
    return render(request,'defects/defect.html',{'defects':defects})

def defect_description(request,id=0):
    defe = Defect.objects.get(id=id)
    images = Defects_screen_shots.objects.filter(defect=defe)
    context = {
        'defe':defe,
        'images':images
    }
    
    return render(request,'defects/description.html',{'context':context})

def add_defect(request):
    items = AddDefectForm()
    if request.method == 'POST':
        items = AddDefectForm(request.POST)
        if items.is_valid():
            items.save()
            return redirect('defect')
    return render(request,'defects/add_defects.html',{'items':items})