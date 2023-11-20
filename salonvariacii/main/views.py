from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import FeedbackForm
import telebot
from decouple import config

def get_url_youtube(url):
    if(url.rfind('share') != -1):
        questionMark = url.rfind('?')
        slash = url.rfind('/')
        return url[slash+1:questionMark]        
    elif(url.rfind('v=') != -1): 
        return url.split("v=")[1]
    else:
        slash = url.rfind('/')
        return url[slash+1:]


def main(request):
    sliderPhoto = MainPageCarousel.objects.all().order_by('show_number')
    about = AboutUs.objects.first()
    aboutMini = AboutUsDopBlock.objects.all().order_by('show_number')
    numberOfBlocksAboutMini = aboutMini.count() 
    catalog_carousel = Kitchen.objects.exclude(show_number=None).order_by('show_number')[:5]  
    reviews = ReviewsAndProject.objects.all()
    look_at = LookAt.objects.all().exclude(show_number=None).order_by('show_number')
    feedbackForm = FeedbackForm()
    title = "TITLEMAIN"
    pageDescription = "pageDescription"
    keyWords = "keyWords"

    data = {
        "sliderPhoto": sliderPhoto,
        "about": about,
        "aboutMini": aboutMini,
        "numberOfBlocksAboutMini": numberOfBlocksAboutMini,
        "catalog_carousel": catalog_carousel,
        "reviews": reviews,
        "look_at": look_at,
        "feedbackForm": feedbackForm,
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
    }

    return render(request, "main/index.html", data)


def catalog(request):
    kitchen = Kitchen.objects.all().order_by('show_number')
    for kit in kitchen:
        kit.catalogVideo = get_url_youtube(kit.catalogVideo)
    openingMethod = KitchenOpeningMethod.objects.values("name").distinct()
    material = KitchenMaterial.objects.values("name").distinct()
    style = KitchenStyle.objects.values("name").distinct()
    feedbackForm = FeedbackForm()
    title = "TITLEMAIN"
    pageDescription = "pageDescription"
    keyWords = "keyWords"
    data = {
        "kitchen": kitchen,
        "openingMethod": openingMethod,
        "material": material,
        "style": style,
        "feedbackForm": feedbackForm,
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
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
    kitchen.kitchenCardVideo = get_url_youtube(kitchen.kitchenCardVideo)
    feedbackForm = FeedbackForm()
    title = "TITLEMAIN"
    pageDescription = "pageDescription"
    keyWords = "keyWords"
    data = {
        "kitchen": kitchen,
        "feedbackForm": feedbackForm,
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
    }
    return render(request, "main/kitchenCard.html", data) 