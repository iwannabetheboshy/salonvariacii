from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import KitchenStyle, KitchenMaterial, KitchenOpeningMethod, FeedBack
from django.core.exceptions import ValidationError


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
   
class FeedbackForm(ModelForm):
   class Meta:
        model = FeedBack
        fields = ['name', 'number', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'required': 'true',
            }),

            "number": TextInput(attrs={
                'class': 'form-control fb_phone',
                'required': 'true',
                'type': 'tel',
                'placeholder': '+7 ',
                'pattern': r'^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$',
                'title': '+7 (XXX) XXX-XX-XX',
            }),
            "message": Textarea(attrs={
                'class': 'form-control-area',
                'placeholder': 'Введите текст сообщения',
            }),
        }
