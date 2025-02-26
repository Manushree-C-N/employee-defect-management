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

class Defect_Edit_Form(forms.ModelForm):
    defect_id = forms.CharField(max_length=100,disabled=True)
    defect_type = forms.CharField(disabled=True)
    class Meta:
        model = Defect
        fields = "__all__"
