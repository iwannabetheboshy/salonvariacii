from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import FilterForm, FeedbackForm


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
    form = FilterForm()
    return render(request, "main/catalog.html", {'kitchen': kitchen, 'form': form})


def filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        kitchen = Kitchen.objects.all()
        if form.is_valid():
            name_value = form.cleaned_data.get('name')
            style_values = form.cleaned_data.get('style', [])
            material_values = form.cleaned_data.get('material', [])
            openingMethod_values = form.cleaned_data.get('openingMethod', [])

            filter_parameters = {
                'name__icontains': name_value,
                'style__in': style_values,
                'material__name__in': material_values,
                'openingMethod__name__in': openingMethod_values,
            }

            kitchen = Kitchen.objects.all()
            for field, values in filter_parameters.items():
                if values:
                    kitchen = kitchen.filter(**{field: values}).values('name','style__name', 'material__name', 'openingMethod__name')

            filtered_kitchens = list(kitchen)  # Преобразование queryset в список словарей
            print(filtered_kitchens)
            return JsonResponse({'filtered_kitchens': filtered_kitchens})
        else:
            # Вывод ошибок в консоль
            print(form.errors)
            return render(request, "main/catalog.html")


def kitchenCard(request, slug):
    kitchen = Kitchen.objects.get(slug=slug)
    data = {
        "kitchen": kitchen,
    }
    return render(request, "main/kitchenCard.html", data)