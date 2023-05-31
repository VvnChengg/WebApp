from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('user/', views.user_interface, name='user'),
    path('create/', views.create, name='create'),
    path('create_interface/', views.create_interface, name='create_interface'),
    path('<category>/', views.market_index, name='category'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
