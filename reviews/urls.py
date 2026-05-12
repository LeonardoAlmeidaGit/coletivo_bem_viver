from django.urls import path
from . import views

urlpatterns = [
    path('<int:kitchen_id>/list/', views.ReviewListView.as_view(), name='review_list'),
    path('create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/detail/', views.ReviewDetailView.as_view(), name='review_detail'),
]
