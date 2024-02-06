from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import FeedbackForm
import telebot
from decouple import config

def page_not_found_view(request, exception):
    return render(
        request,
        "404.html",
        {
            "feedbackForm": FeedbackForm(),
            "header": Header.objects.first(),
            "footer": Footer.objects.first(),
            "feedbackFile": Politic.objects.first(),
            "title": f"Похоже мы не нашли что вы искали",
            "description": "Заказать итальянскую кухонную мебель и гарнитур во Владивостоке. Современная или классическая кухня. Дизайн под заказ. Можем изготовить по индивидуальным размерам с установкой",
            "keywords": "итальянские кухни, итальянская кухня фото,  кухня в итальянском стиле фото, купить итальянскую кухню, кухня в итальянском стиле, кухонная мебель италии, ручки для кухонной мебели италия, современные итальянские кухни, кухонный гарнитур италия, итальянская кухня цена, итальянская мебель для кухни, купить кухню, купить кухню под заказ, кухня из дерева купить, мебель для кухни, купить мебель для кухни, сайт мебели для кухни, мебель для кухни фото и цены, кухня фото дизайн, заказать индивидуальную кухню, заказать кухню по индивидуальным размерам",
        },status=404
    )

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
    for slide in sliderPhoto:
        slide.name = slide.name.title()
    about = AboutUs.objects.first()
    catalog_carousel = Kitchen.objects.exclude(show_number=None).exclude(hide=True).order_by('show_number')[:5]  
    for kit in catalog_carousel:
        kit.name = kit.name.capitalize()
    look_at = LookAt.objects.all().exclude(show_number=None).exclude(hide=True).order_by('show_number')
    for look_at_item in look_at:
        if look_at_item.shorts:
            look_at_item.shorts = get_url_youtube(look_at_item.shorts) 
    watchVideoMain = WatchVideoMain.objects.first()
    watchVideoMain.url = get_url_youtube(WatchVideoMain.objects.first().url) 
    title = "Итальянские кухни Stosa Cucine - на заказ  по индивидуальным размерам во Владивостоке"
    pageDescription = "Современные и классические кухни итальянской фабрики Stosa под заказ во Владивостоке. Высококачественная кухня  из Италии, оригинальный дизайн и нестандартные решения"
    keyWords = "итальянские кухни, итальянская кухня фото,  кухня в итальянском стиле фото, купить итальянскую кухню, кухня в итальянском стиле, кухонная мебель италии, ручки для кухонной мебели италия, современные итальянские кухни, кухонный гарнитур италия, итальянская кухня цена, итальянская мебель для кухни, купить кухню, купить кухню под заказ, кухня из дерева купить, мебель для кухни, купить мебель для кухни, сайт мебели для кухни, мебель для кухни фото и цены, кухня фото дизайн, заказать индивидуальную кухню, заказать кухню по индивидуальным размерам"

    data = {
        "sliderPhoto": sliderPhoto,
        "about": about,
        "catalog_carousel": catalog_carousel,
        "look_at": look_at,
        "feedbackForm": FeedbackForm(),
        "feedbackFile": Politic.objects.first(),
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
        "advantagesTitle": AdvantagesTitle.objects.first(),
        "AdvantagesBlocks": AdvantagesBlocks.objects.order_by('show_number'),
        "LookAtTitle": LookAtTitle.objects.first(),
        "FeedbackBlock": FeedbackBlock.objects.first(),
        "watchVideoMain": watchVideoMain,
        "catalogMain":CatalogMain.objects.first(),
        "сatalogMainBlock":CatalogMainBlock.objects.first(),
        "moreMainBlock":MoreMainBlock.objects.first(),
        "moreBlocks":MoreBlocks.objects.order_by('showNumber'),
        "header": Header.objects.first(),
        "footer": Footer.objects.first(),
    }


    return render(request, "main/index.html", data)


def catalog(request):
    kitchen = Kitchen.objects.exclude(hide=True).order_by('show_number')
    for kit in kitchen:
        if kit.catalogVideo:
            kit.catalogVideo = get_url_youtube(kit.catalogVideo)
        kit.name = kit.name.title()
    catalogTitle = CatalogTitle.objects.first(),
    openingMethod = KitchenOpeningMethod.objects.values("name").distinct()
    material = KitchenMaterial.objects.values("name").distinct()
    style = KitchenStyle.objects.values("name").distinct()
    title = "Каталог кухонь из Италии. Купить кухню во Владивостоке. Stosa Cucine"
    pageDescription = "Каталог итальянских кухонь Stosa Cucine. Кухни на заказ по индивидуальным размерам. Отделка и материал на выбор. Встраиваемые кухонные гарнитуры, различные системы открывания"
    keyWords = "итальянские кухни, итальянская кухня фото,  кухня в итальянском стиле фото, купить итальянскую кухню, кухня в итальянском стиле, кухонная мебель италии, ручки для кухонной мебели италия, современные итальянские кухни, кухонный гарнитур италия, итальянская кухня цена, итальянская мебель для кухни, купить кухню под заказ, кухня из дерева купить, мебель для кухни, купить мебель для кухни, сайт мебели для кухни, мебель для кухни фото и цены, кухня фото дизайн, заказать индивидуальную кухню, заказать кухню по индивидуальным размерам,"
    data = {
        "kitchen": kitchen,
        "openingMethod": openingMethod,
        "material": material,
        "style": style,
        "feedbackForm": FeedbackForm(),
        "feedbackFile": Politic.objects.first(),
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
        "FeedbackBlock": FeedbackBlock.objects.first(),
        "catalogTitle": catalogTitle[0],
        "header": Header.objects.first(),
        "footer": Footer.objects.first(),
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
            bot.send_message(629793380, 'Имя: {0}\nТелефон: {2}\nСообщение: {1}'.
                             format(form.cleaned_data['name'], form.cleaned_data['message'], form.cleaned_data['number'], ))
            bot.send_message(1215051253, 'Имя: {0}\nТелефон: {2}\nСообщение: {1}'.
                             format(form.cleaned_data['name'], form.cleaned_data['message'], form.cleaned_data['number'], ))
            return HttpResponse("Заявка отправлена! Мы скоро перезвоним вам")


def kitchenCard(request, slug):
    kitchen = Kitchen.objects.get(slug=slug)
    if kitchen.show_number == Kitchen.objects.order_by('-show_number').first().show_number:
       next_kitchen = Kitchen.objects.exclude(hide=True).order_by('show_number').first()
    else:
        next_kitchen = Kitchen.objects.exclude(hide=True).filter(show_number__gt=kitchen.show_number).order_by('show_number').first()
    kitchen.name = kitchen.name.title()
    kitchen.kitchenCardVideo = get_url_youtube(kitchen.kitchenCardVideo)
    if kitchen.kitchenCardVideo:
        kitchen.kitchenCardVideo = get_url_youtube(kitchen.kitchenCardVideo)
    descriptionStyle = (
        "современном" if str(kitchen.style).strip() == "Современный стиль" else
        "классическом" if str(kitchen.style).strip() == "Классический стиль" else
        "современном, классическом"
    )
    title = "Итальянская кухня Stosa " +  kitchen.name + ". Индивидуальные размеры, отделка на выбор. Stosa Cucine"
    pageDescription = "Stosa " + kitchen.name + ". Мебель для кухни Stosa Cucine. Качественный кухонный гарнитур, индивидуальный проект. Кухни в " + descriptionStyle + ' стиле. ' + ', '.join([str(mat) for mat in kitchen.material.all()])
    keyWords =  "Stosa " + kitchen.name + ", " + ', '.join([str(mat) for mat in kitchen.material.all()])  +', '+ ', '.join([str(mat) for mat in kitchen.openingMethod.all()]) +', ' +', '.join([str(mat) for mat in kitchen.finishing.all()]) + ', ' + ', '.join([str(color) for mat in kitchen.finishing.all() for color in mat.colors.all()])
    data = {
        "kitchen": kitchen,
        "feedbackForm": FeedbackForm(),
        "feedbackFile": Politic.objects.first(),
        "title": title,
        "pageDescription": pageDescription,
        "keyWords": keyWords,
        "FeedbackBlock": FeedbackBlock.objects.first(),
        "kitchenCardText": KitchenCardText.objects.first(),
        "certificate": Certificate.objects.all(),
        "header": Header.objects.first(),
        "footer": Footer.objects.first(),
        "nextKitchen": next_kitchen,
    }
    return render(request, "main/kitchenCard.html", data) 