from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('catalog/', views.catalog),
    path('feedback/', views.sendFeedBack),
    path('get-related-items-for-admin/', views.get_related_items_for_admin),
    path('kitchen/<slug:slug>', views.kitchenCard),
]
