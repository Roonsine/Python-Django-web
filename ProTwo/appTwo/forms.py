from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    #define fields and validation here
    class Meta():
        model = User
        fields = '__all__'
