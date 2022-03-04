from django.urls import path
from assortment.views.drink import DrinkAPIView
from assortment.views.list_views import DrinkListAPIView, PizzaListAPIView
from assortment.views.pizza import PizzaAPIView

urlpatterns = [
    path('pizza/', PizzaListAPIView.as_view()),
    path('pizza/<slug:slug>/', PizzaAPIView.as_view()),
    path('drink/', DrinkListAPIView.as_view()),
    path('drink/<slug:slug>/', DrinkAPIView.as_view()),
]
