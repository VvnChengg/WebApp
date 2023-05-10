from django.urls import path, re_path
from . import views  #引用這個資料夾中的views檔案
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "item_list"),
    path('posts/', views.add_item, name='add_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    # re_path(r'^item/$', views.item_detail, name='item_detail'),
    path('<str:category>/', views.index, name='item_list_by_category'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)