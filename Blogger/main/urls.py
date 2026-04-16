from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('posts/', views.posts_view, name='posts_view'),
    path('create/', views.create_post_view, name='create_post_view'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail_view'),
    path('posts/<int:post_id>/edit/', views.edit_post_view, name='edit_post_view'),
    path('posts/<int:post_id>/delete/', views.delete_post_view, name='delete_post_view'),
    path('mode/<mode>/', views.mode_view, name='mode_view'),
]