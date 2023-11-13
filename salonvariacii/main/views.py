from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import FeedbackForm
import telebot
from decouple import config


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
    look_at = LookAt.objects.all().exclude(show_number=None).order_by('show_number')
    feedbackForm = FeedbackForm()
    
    data = {
        "sliderPhoto": sliderPhoto,
        "about": about,
        "aboutMini": aboutMini,
        "numberOfBlocksAboutMini": numberOfBlocksAboutMini,
        "catalog_carousel": catalog_carousel,
        "reviews": reviews,
        "look_at": look_at,
        "feedbackForm": feedbackForm,
    }

    return render(request, "main/index.html", data)


def catalog(request):
    kitchen = Kitchen.objects.all()
    openingMethod = KitchenOpeningMethod.objects.values("name").distinct()
    material = KitchenMaterial.objects.values("name").distinct()
    style = KitchenStyle.objects.values("name").distinct()
    feedbackForm = FeedbackForm()
    data = {
        "kitchen": kitchen,
        "openingMethod": openingMethod,
        "material": material,
        "style": style,
        "feedbackForm": feedbackForm,
    }
    return render(request, "main/catalog.html", data)


def sendFeedBack(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            f = FeedBack(
                name=form.cleaned_data['name'],
                number=form.cleaned_data['number'],
                message=form.cleaned_data['message'])
            f.save()
            
            bot = telebot.TeleBot(config('BotToken'))
            bot.send_message(1029774332, 'Имя: {0}\nТелефон: {2}\nСообщение: {1}'.
                             format(form.cleaned_data['name'], form.cleaned_data['message'], form.cleaned_data['number'], ))
            return HttpResponse("Заявка отправлена! Мы скоро перезвоним вам")


def kitchenCard(request, slug):
    kitchen = Kitchen.objects.get(slug=slug)
    feedbackForm = FeedbackForm()
    return render(request, "main/kitchenCard.html", {"kitchen": kitchen, "feedbackForm": feedbackForm}) 