from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='photos_home'),
    path('about/', views.about, name='photos_about'),
    path('gallery/', views.gallery, name='photos_gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='photos_photo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)