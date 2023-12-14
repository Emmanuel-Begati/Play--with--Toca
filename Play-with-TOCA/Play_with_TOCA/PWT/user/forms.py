from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    age = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        # Remove validation messages
        for field_name in self.fields:
            self.fields[field_name].error_messages = {'required': None} 