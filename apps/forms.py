from django import forms

from apps.models import Class, Instance


class ClassForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Class Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Animal'
            }
        ),
        help_text='Enter the name of the class'
    )

    class Meta:
        model = Class
        fields = ['name']


class InstanceForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Instance Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Alpaca'
            }
        ),
        help_text='Enter the name of the instance'
    )

    class_instance = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Select the class that this instance will be in'
    )

    class Meta:
        model = Instance
        fields = ['name', 'class_instance']
