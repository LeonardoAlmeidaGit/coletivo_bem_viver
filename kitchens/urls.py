from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.KitchenListView.as_view(), name='kitchen_list'),
    path('create/', views.KitchenCreateView.as_view(), name='kitchen_create'),
    path('<int:pk>/detail/', views.KitchenDetailView.as_view(), name='kitchen_detail'),
    path('<int:pk>/update/', views.KitchenUpdateView.as_view(), name='kitchen_update'),
]
