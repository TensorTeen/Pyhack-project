from cProfile import label
from dataclasses import fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ['username','email','password1','password2'] 

class Test_TextForm(forms.Form) :
    Test_Text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":200}),initial='Type Here',label=False)

class TrainForm(forms.Form):
    modelname = forms.CharField(label='Model Name : ')
    epoch = forms.IntegerField(label='Epochs : ')
    batch_size = forms.IntegerField(label='Batch Size : ')

