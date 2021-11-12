from typing import Optional
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import RobotConfirmationViews, User,Order,Review,ContestEntries, WithdrawAmount,Package_form

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    Is_worker = forms.BooleanField(
        required=False,
        widget= forms.CheckboxInput(
            attrs={
                "class": "checkbox" 
            }
        )
    )
    Is_client = forms.BooleanField(
        required=False,
        widget= forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','Is_worker', 'Is_client']
        
class AddOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['url','category','quantity','id_name','phone_no','img']

class AddPackage_form(forms.ModelForm):
    
    class Meta:
        model = Package_form
        fields = ['url','p_category','id_name','phone_no','img']
      
class AddReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['details','rating']
        
class ContestSubmitionForm(forms.ModelForm):
    
    class Meta:
        model = ContestEntries
        fields = ['whatsapp','facebook','twitter']
        
class RobotConfirmationForm(forms.ModelForm):
    
    class Meta:
        model = RobotConfirmationViews
        fields = ['entry_code']
        
class WithdrawForm(forms.ModelForm):
    
    class Meta:
        model = WithdrawAmount
        fields = ['payment_method','acc_number','amount']