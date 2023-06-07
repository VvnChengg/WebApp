# chat/urls.py
from django.urls import path, include
from . import views as chat_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", chat_views.chat_index, name="chat_index"),
    path("<str:username>", chat_views.room, name="room"),
    path("<str:username>/send_message", chat_views.send_message, name="send_message"),
    path("search_user", chat_views.search_user, name="search_user"),
]
