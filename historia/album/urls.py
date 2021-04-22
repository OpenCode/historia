from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>', views.category, name='category'),
    path('document/<int:document_id>', views.document, name='document'),
]
