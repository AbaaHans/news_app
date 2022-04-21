from logging import Handler
from django import views
from django.urls import path
from .import views
from django.conf import settings
from django.conf .urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
    path('all-news/', views.All_new, name='all-news'),
    path('detail/<int:id>', views.Detail, name='detail'),
    path('categories', views.All_category, name='categories'),
    path('category-infos/<int:id>', views.Categorie_infos, name='category-infos'),
    # path('international/', views.International,name='international')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


