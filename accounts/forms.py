from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField
    )
from django.contrib.auth import get_user_model
from django import forms

from store.models import Customer



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 
               'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
        }
))

class EditCustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer
        fields = ['name', 'email', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(EditCustomerForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        

        