from django.forms import forms
from assetapp.models import Assets,Assets_types

class Assets(forms.ModelForms):
    class Meta:
        Model=Assets
        fields='__all__'

class EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')

class Assets_types(forms.ModelForms):
    class Meta:
        model=Assets_types
        fields='__all__'
