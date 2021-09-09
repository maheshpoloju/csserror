from django.urls import path
from . import views
from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('hydjobs/', views.hydjobs1),
    path('blorejobs/', views.blorejobs),
    path('punejobs/', views.punejobs),
    path('chennaijobs/', views.chennaijobs),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)