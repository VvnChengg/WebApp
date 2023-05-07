from django.urls import path
from . import views  #引用這個資料夾中的views檔案
from django.conf import settings
from django.conf.urls.static import static
from .views import item＿detail

urlpatterns = [
    path('', views.index, name = "Index"),
    path('posts/', views.add_item, name='add_item'),
    # path('item/<int:item_id>/', item_detail, name='item_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)