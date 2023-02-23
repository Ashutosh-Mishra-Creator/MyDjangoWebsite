from django.urls import path
from . import views

#ALWAYS END OUR ROUTEES WITH A /
urlpatterns = [
    path('hello/', views.say_hello)
]