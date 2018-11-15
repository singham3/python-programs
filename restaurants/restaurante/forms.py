from django import forms
from .models import Send_Message

class Send_us_Message(forms.ModelForm):
    class Meta:
        model = Send_Message
        fields =  ['Full_Name','Phone_Number','Email_Address','Message' ]