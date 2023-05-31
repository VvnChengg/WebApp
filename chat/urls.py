# chat/urls.py
from . import views
from django.urls import path, include
from chat import views as chat_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>", views.room, name="room"),
    path("<str:username>/send_message", views.send_message, name="send_message"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)