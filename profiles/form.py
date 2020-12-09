from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=65, required=True, widget=forms.EmailInput())
    dob=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','dob','city','adress','pincode','user_type','gender','password1', 'password2')