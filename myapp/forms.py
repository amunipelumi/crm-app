
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Record



# register/create
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# add new record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
    

# update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']