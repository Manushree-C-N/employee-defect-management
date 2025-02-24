from django import forms 
from DefectsPortal.models import Defect


class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ['defect_id','defect_name','defect_type','assigned_by','assigned_to','description','priority']

class AddDefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = "__all__"
