from django import forms
from .models import Programming_Competition, NOSKode

class Programming_Competition_Form(forms.ModelForm):
    field_order = ['full_name','email','phone_no','programming_language']
    class Meta:
        model = Programming_Competition
        fields = {'full_name','email','phone_no','programming_language'}

class NOSKode_Form(forms.ModelForm):
    field_order = ['team_name','total_team_members','team_leader','phone_number','email','project_title','project_description']
    class Meta:
        model = NOSKode
        fields = {'team_name','total_team_members','team_leader','phone_number','email','project_title','project_description'}
