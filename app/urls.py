from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('adopt/', views.AdoptView.as_view(), name='adopt'),
    path('adopt/edit/', views.AdoptCreate.as_view(), name='create'),
    path('adopt/edit/<int:pk>/', views.AdoptUpdate.as_view(), name='update'),
    path('adopt/edit/<int:pk>/delete', views.AdoptDelete.as_view(), name='delete'),
    path('adopt/<str:species>/', views.AdoptView.as_view(), name='adopt_species'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
