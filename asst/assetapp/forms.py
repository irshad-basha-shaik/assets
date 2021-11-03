from django.forms import forms
from .models import Assets,Assets_types,Ops,Acategory,Astatus,Location,Software

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

class Ops(forms.ModelForms):
    class Meta:
        model=Ops
        fields='__all__'
class Ops_EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')

class Acategory(forms.ModelForms):
    class Meta:
        Model=Acategory
        fields='__all__'
class Acategory_EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')


class Astatus(forms.ModelForms):
    class Meta:
        Model=Astatus
        fields='__all__'

class Astatus_EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')


class Location(forms.ModelForms):
    class Meta:
        Model=Location
        fields='__all__'
class Location_EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')

class Software(forms.ModelForms):
    class Meta:
        model=Software
        fields='__all__'
class Software_EditForm(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')