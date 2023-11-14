from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import FeedBack
   
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
    
   def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        # Удаление id для каждого поля
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['id'] = ''