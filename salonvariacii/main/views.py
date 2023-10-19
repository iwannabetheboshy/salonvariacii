from django.http import JsonResponse
from django.shortcuts import render
from .models import Kitchen
from .forms import FilterForm


def main(request):
    return render(request, "main/catalog.html")


def catalog(request):
    kitchen = Kitchen.objects.all()
    form = FilterForm()
    return render(request, "main/catalog.html", {'kitchen': kitchen, 'form': form})


def filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        kitchen = Kitchen.objects.all()
        if form.is_valid():
            color_values = form.cleaned_data.get('color', [])
            style_values = form.cleaned_data.get('style', [])
            material_values = form.cleaned_data.get('material', [])
            form_values = form.cleaned_data.get('form', [])

            filter_parameters = {
                'color__in': color_values,
                'style__in': style_values,
                'material__in': material_values,
                'form__in': form_values,
            }

            kitchen = Kitchen.objects.all()
            for field, values in filter_parameters.items():
                if values:
                    kitchen = kitchen.filter(**{field: values})

            filtered_kitchens = list(kitchen.values())  # Преобразование queryset в список словарей

            return JsonResponse({'filtered_kitchens': filtered_kitchens})

