from django import forms
from .models import Kitchen

#
# class FilterForm(forms.Form):
#     color = forms.MultipleChoiceField(choices=Kitchen.COLOR_CHOICES, widget=forms.CheckboxSelectMultiple,
#                                       required=False, label="Цвет")
#     style = forms.MultipleChoiceField(choices=Kitchen.STYLE_CHOICES, widget=forms.CheckboxSelectMultiple,
#                                       required=False, label="Стиль")
#     material = forms.MultipleChoiceField(choices=Kitchen.MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple,
#                                          required=False, label="Материал")
#     form = forms.MultipleChoiceField(choices=Kitchen.FORM_CHOICES, widget=forms.CheckboxSelectMultiple,
#                                      required=False, label="Форма")
#     width = forms.IntegerField(required=False, label="Ширина")

