from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('catalog/', views.catalog),
    path('filter/', views.filter),

]
