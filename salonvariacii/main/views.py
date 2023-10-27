from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# from .forms import FilterForm


def get_related_items_for_admin(request):
    style_id = request.GET.get('style_id')

    materials = KitchenMaterial.objects.filter(kitchen_styles__pk=style_id)
    opening_methods = KitchenOpeningMethod.objects.filter(kitchen_styles__pk=style_id)

    material_data = [{'id': material.id, 'name': material.name} for material in materials]
    opening_method_data = [{'id': opening_method.id, 'name': opening_method.name} for opening_method in opening_methods]

    response_data = {
        'materials': material_data,
        'opening_methods': opening_method_data,
    }

    return JsonResponse(response_data)


def main(request):
    return render(request, "main/catalog.html")


def catalog(request):
    kitchen = Kitchen.objects.all()
    # form = FilterForm()
    return render(request, "main/catalog.html", {'kitchen': kitchen})


def filter(request):
    # if request.method == 'POST':
    #     form = FilterForm(request.POST)
    #     kitchen = Kitchen.objects.all()
    #     if form.is_valid():
    #         color_values = form.cleaned_data.get('color', [])
    #         style_values = form.cleaned_data.get('style', [])
    #         material_values = form.cleaned_data.get('material', [])
    #         form_values = form.cleaned_data.get('form', [])
    #
    #         filter_parameters = {
    #             'color__in': color_values,
    #             'style__in': style_values,
    #             'material__in': material_values,
    #             'form__in': form_values,
    #         }
    #
    #         kitchen = Kitchen.objects.all()
    #         for field, values in filter_parameters.items():
    #             if values:
    #                 kitchen = kitchen.filter(**{field: values})
    #
    #         filtered_kitchens = list(kitchen.values())  # Преобразование queryset в список словарей
    #
    #         return JsonResponse({'filtered_kitchens': filtered_kitchens})
    return render(request, "main/catalog.html")
