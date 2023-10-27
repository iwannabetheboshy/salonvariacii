from django import forms
from .models import KitchenStyle, KitchenMaterial, KitchenOpeningMethod


class FilterForm(forms.Form):
   name = forms.CharField(label="Наименование", required=False)
   style = forms.ModelMultipleChoiceField(queryset=KitchenStyle.objects.all(), widget=forms.CheckboxSelectMultiple,
                                          required=False, label="Стиль кухни")

   material = forms.MultipleChoiceField(choices=KitchenMaterial.objects.values_list("name", "name").distinct(),
                                             widget=forms.CheckboxSelectMultiple, required=False,
                                             label="Материал кухни")
   openingMethod = forms.MultipleChoiceField(choices=KitchenOpeningMethod.objects.values_list("name", "name").distinct(),
                                                  widget=forms.CheckboxSelectMultiple, required=False,
                                                  label="Метод открытия кухни")
