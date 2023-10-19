from django import forms
from .models import Kitchen


class FilterForm(forms.Form):
    color = forms.MultipleChoiceField(choices=Kitchen.COLOR_CHOICES, widget=forms.CheckboxSelectMultiple,
                                      required=False)
    style = forms.MultipleChoiceField(choices=Kitchen.STYLE_CHOICES, widget=forms.CheckboxSelectMultiple,
                                      required=False)
    material = forms.MultipleChoiceField(choices=Kitchen.MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple,
                                         required=False)
    form = forms.MultipleChoiceField(choices=Kitchen.FORM_CHOICES, widget=forms.CheckboxSelectMultiple,
                                     required=False)
    width = forms.IntegerField(required=False)

