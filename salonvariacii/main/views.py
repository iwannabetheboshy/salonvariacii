from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import FilterForm, FeedbackForm
import json


def get_related_items_for_admin(request):
    selected_styles = request.GET.get('styles')
    selected_styles = selected_styles.split(',')

    materials = KitchenMaterial.objects.filter(kitchen_styles__pk__in=selected_styles)
    opening_methods = KitchenOpeningMethod.objects.filter(kitchen_styles__pk__in=selected_styles)

    material_data = [{'id': material.id, 'name': material.name} for material in materials]
    opening_method_data = [{'id': opening_method.id, 'name': opening_method.name} for opening_method in opening_methods]

    response_data = {
        'materials': material_data,
        'opening_methods': opening_method_data,
    }

    return JsonResponse(response_data)


def main(request):
    sliderPhoto = MainPageCarousel.objects.all().order_by('show_number')
    about = AboutUs.objects.first()
    aboutMini = AboutUsDopBlock.objects.all()
    numberOfBlocksAboutMini = aboutMini.count() 
    catalog_carousel = Kitchen.objects.exclude(show_number=None).order_by('show_number')
    reviews = ReviewsAndProject.objects.all()
    feedbackForm = FeedbackForm()
    
    
    data = {
        "sliderPhoto": sliderPhoto,
        "about": about,
        "aboutMini": aboutMini,
        "numberOfBlocksAboutMini": numberOfBlocksAboutMini,
        "catalog_carousel": catalog_carousel,
        "reviews": reviews,
        "feedbackForm": feedbackForm,
    }

    return render(request, "main/index.html", data)


def catalog(request):
    kitchen = Kitchen.objects.all()
    openingMethod = KitchenOpeningMethod.objects.values("name").distinct()
    material = KitchenMaterial.objects.values("name").distinct()
    style = KitchenStyle.objects.values("name").distinct()
    form = FilterForm()
    data = {
        "kitchen": kitchen,
        "form": form,
        "openingMethod": openingMethod,
        "material": material,
        "style": style,
    }
    return render(request, "main/catalog.html", data)


def filter(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        style_values = data.get('style', [])
        material_values = data.get('material', [])
        openingMethod_values = data.get('openingMethod', [])
        search = data.get('search', [])
        
        if not style_values and not material_values and not openingMethod_values and not search:
            kitchen = Kitchen.objects.all().values('name', 'slug', 'mainImage', 'catalogVideo')
            filtered_kitchens = list(kitchen)
        else:
            kitchen = Kitchen.objects.all()
            filter_parameters = {
                'name__icontains': search,
                'style__name': style_values,
                'material__name': material_values,
                'openingMethod__name': openingMethod_values,
            }

            kitchen = Kitchen.objects.all()

            for field, values in filter_parameters.items():
                if values:
                    #если в фильтрации несколько значений по одному полю
                    if isinstance(values, list):
                        kitchen = kitchen.filter(**{field + '__in': values}).values('name', 'slug', 'mainImage', 'catalogVideo')
                    else:
                        kitchen = kitchen.filter(**{field : values}).values('name', 'slug', 'mainImage', 'catalogVideo')

            filtered_kitchens = list(kitchen)
       
        return JsonResponse({'filtered_kitchens': filtered_kitchens})

def kitchenCard(request, slug):
    kitchen = Kitchen.objects.get(slug=slug)
    return render(request, "main/kitchenCard.html", {"kitchen": kitchen}) 