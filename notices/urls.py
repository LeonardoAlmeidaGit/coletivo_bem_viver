from django.urls import path
from . import views

urlpatterns = [
    path('<int:kitchen_id>/list/', views.NoticeListView.as_view(), name='notice_list'),
    path('create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>/update/', views.NoticeUpdateView.as_view(), name='notice_update'),
    path('<int:pk>/delete/', views.NoticeDeleteView.as_view(), name='notice_delete'),
]
