#La idea de este archivo es que ejecute lo mismo que src.urls.py

from django.urls import path

from .consumers import JokesConsumer

#Websockets Urlpatterns
ws_urlpatterns = [
    path('ws/jokes/', JokesConsumer.as_asgi()),
]