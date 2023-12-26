from django import forms

from apps.models import Class, Instance, InstanceInstanceConnection, RAW_TYPE_CHOICES, PropertyType


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

    def clean(self):
        cleaned_data = super(ClassForm, self).clean()
        name = cleaned_data.get("name")
        exist_class = Class.objects.filter(name=name)
        if exist_class.exists():
            self.add_error('name', f'The class with name {name} already exists')
        return cleaned_data


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

    def clean(self):
        cleaned_data = super(InstanceForm, self).clean()
        name = cleaned_data.get("name")
        class_instance = cleaned_data.get("class_instance")
        exist_instance = Instance.objects.filter(name=name, class_instance=class_instance)
        if exist_instance.exists():
            raise forms.ValidationError(
                f"The instance with name {name} already exists in {class_instance}",
                code='invalid'
            )
        return cleaned_data


class InstanceInstanceConnectionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Connection Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Eats'
            }
        ),
        help_text='Enter the name of the connection'
    )

    first_instance_class = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label='From Class',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Select the first class that this connection will be in'
    )

    second_instance_class = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label='To Class',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Select the second class that this connection will be in'
    )

    class Meta:
        model = InstanceInstanceConnection
        fields = ['name', 'first_instance_class', 'second_instance_class']

    def clean(self):
        cleaned_data = super(InstanceInstanceConnectionForm, self).clean()
        first_instance_class = cleaned_data.get("first_instance_class")
        second_instance_class = cleaned_data.get("second_instance_class")
        exist_connection = InstanceInstanceConnection.objects.filter(first_instance_class=first_instance_class, second_instance_class=second_instance_class)
        if exist_connection.exists():
            raise forms.ValidationError(
                f"The connection between {first_instance_class} and {second_instance_class} already exists ({exist_connection.first().name})",
                code='invalid'
            )
        return cleaned_data


class PropertyTypeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Property Type Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'haveLegs'
            }
        ),
        help_text='Enter the name of the property type'
    )

    class_instance = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label='Class',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Select the class that can have this property type'
    )

    raw_type = forms.ChoiceField(
        choices=RAW_TYPE_CHOICES,
        label='Raw Type',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Select the raw type of the property type'
    )

    limitation = forms.JSONField(
        label='Limitation',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Enter the limitation of the property type'
    )

    class Meta:
        model = PropertyType
        fields = ['name', 'class_instance', 'raw_type', 'limitation']

    def clean(self):
        cleaned_data = super(PropertyTypeForm, self).clean()
        name = cleaned_data.get("name")
        raw_type = cleaned_data.get("raw_type")
        class_instance = cleaned_data.get("class_instance")
        exist_property_type = PropertyType.objects.filter(name=name, class_instance=class_instance, raw_type=raw_type)
        if exist_property_type.exists():
            raise forms.ValidationError(
                f"The property type with name {name} already exists in {class_instance} with raw type {raw_type}",
                code='invalid'
            )
        return cleaned_data
