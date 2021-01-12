from django import forms
from django.forms.models import inlineformset_factory
from .models import Field, DataSchema


class DataSchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchema
        fields = '__all__'


FieldFormset = inlineformset_factory(DataSchema, Field, extra=3, fields=['column_name', 'type', 'order', ])