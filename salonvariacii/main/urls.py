from django.urls import path
from . import views
from django.views.static import serve 
from django.conf import settings

urlpatterns = [
    path('', views.main),
    path('catalog/', views.catalog),
    path('feedback/', views.sendFeedBack),
    path('kitchen/<slug:slug>', views.kitchenCard),
]
