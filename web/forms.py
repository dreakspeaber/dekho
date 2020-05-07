from django import forms
from web.models import *
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget



class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'password'})) 
    

class PassForm(forms.Form):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'password'})) 
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control, ',  'placeholder' : 'confirm password'})) 
    

class PercentageForm(forms.Form):
    phonenumber = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'phone number'}))
    percentage = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))


class SalesExecForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'username'})) 
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control',  'placeholder' : 'password'}))
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control, ',  'placeholder' : 'confirm password'})) 
    phonenumber = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'phone number'}))
    percentage = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))



class ServiceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields='__all__'

        widget ={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields='__all__'

        widget ={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

    
class ActivitiesForm(forms.ModelForm):
    class Meta:
        model=Activities
        fields='__all__'

        widget ={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'render_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'loc' : ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'class' : 'form-control'}),
            'service' : ModelSelect2Widget(model=Services,search_fields=['name__icontains'],attrs={'class' : 'form-control'}), 
            'price' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

    

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        exclude= ['price','has_closed','cut','time','user']
        widgets = {
            'customer':forms.TextInput(attrs={'class' : 'form-control'}),
            'heading':forms.TextInput(attrs={'class' : 'form-control'}),
            'loc1':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities1':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc2':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities2':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc3':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities3':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc4':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities4':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc5':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities5':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc6':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities6':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc7':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities7':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc8':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities8':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc9':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities9':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'loc10':ModelSelect2Widget(model=Location,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}),
            'activities10':ModelSelect2MultipleWidget(model=Activities,search_fields=['name__icontains'],attrs={'height':'3','class' : 'form-control'}), 
        }


class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields='__all__'

        widget ={
            'content' : forms.Textarea(attrs={'rrows' : 3,'id':'e2','class' : 'form-control'}),
        }
