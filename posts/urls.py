from django.urls import path, re_path
from . import views  #引用這個資料夾中的views檔案
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "item_list"),
    path('sell/', views.add_item, name='add_item'),
    path('my-item/', views.my_item, name='my_item'),
    path('my-item/delete-item/<int:item_id>', views.delete_item, name='delete_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('<str:category>/', views.index, name='item_list_by_category'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)