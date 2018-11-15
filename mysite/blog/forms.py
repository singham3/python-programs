from django import forms
from .models import bloginfo

class blogform(forms.ModelForm):
    class Meta:
        model = bloginfo
        fields =  ['name','value','material','location','image_url' ]