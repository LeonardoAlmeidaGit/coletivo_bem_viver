from django.urls import path
from . import views

urlpatterns = [
    path('<int:kitchen_id>/list/', views.MenuListView.as_view(), name='menu_list'),
    path('create/', views.MenuCreateView.as_view(), name='menu_create'),
    path('<int:pk>/update/', views.MenuUpdateView.as_view(), name='menu_update'),
    path('<int:pk>/delete/', views.MenuDeleteView.as_view(), name='menu_delete'),

    path('<int:menu_pk>/item/create/', views.MenuItemCreateView.as_view(), name='menuitem_create'),
    path('<int:menu_pk>/item/<int:pk>/update/', views.MenuItemUpdateView.as_view(), name='menuitem_update'),
    path('<int:menu_pk>/item/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menuitem_delete'),
]
