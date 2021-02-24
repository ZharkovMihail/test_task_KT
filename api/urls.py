from django.urls import path

from . import views

urlpatterns = [
    path('api/images/', views.images1, name='images'),
    path('api/images_by_tags', views.get_images_by_tag, name='get_images_by_tag'),
    path('media/uploads/<str:file_name>', views.get_image, name='get_image'),
]