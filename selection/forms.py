from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Student


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        help_text = {
            'username': 'same as your roll no.',
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    class Meta:
        model = Student
        fields = (
            'student_name',
            'father_name',
            'enrollment_no',
            'course',
            'dob',
            'gender',
        )


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('room',)
