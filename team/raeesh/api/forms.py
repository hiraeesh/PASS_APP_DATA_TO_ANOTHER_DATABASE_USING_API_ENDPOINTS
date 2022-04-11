# Create your models here.
from django import forms
class Stu(forms.Form):
 id = forms.IntegerField()
 name = forms.CharField()
 email = forms.EmailField()
 password = forms.CharField()
