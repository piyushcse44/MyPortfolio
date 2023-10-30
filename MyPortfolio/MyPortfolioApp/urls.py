from django.urls import path
from .views import HomePage,PostForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomePage,name='HomePage'),
    path('api/post/form',PostForm,name='PostForm'),


]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


