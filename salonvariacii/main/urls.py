from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('catalog/', views.catalog),
    path('feedback/', views.sendFeedBack),
    path('kitchen/<slug:slug>', views.kitchenCard),
]
