from django import forms
from .models import profile,paper
class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['Name','Email','Contect','Designation','Organisation','Address','Bio']

class paperform(forms.ModelForm):
    class Meta:
        model=paper
        fields=['Title','Research_field','paper_type','attachment','Keywords','Author']
