from django import forms
from django.contrib.auth.models import User
from .models import profile,paper
class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['Name','Email','Contect','Designation','Organisation','Address','Bio']

class paperform(forms.ModelForm):
    class Meta:
        model=paper
        fields=['Title','Research_field','paper_type','attachment','Keywords','Author']
class loginform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
