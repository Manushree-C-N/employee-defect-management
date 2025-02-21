from django.shortcuts import render
from DefectsPortal.models import Defect

# Create your views here.
def defect(request):
    defects = Defect.objects.all()
    return render(request,'defects/defect.html',{'defects':defects})

def defect_description(request,id=0):
    defe = Defect.objects.get(id=id)
    return render(request,'defects/description.html',{'defe':defe})