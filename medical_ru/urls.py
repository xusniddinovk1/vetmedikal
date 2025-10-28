from django.urls import path
from . import views

app_name = 'medical_ru'

urlpatterns = [
    path('', views.home_page, name='home'),
    path("о_нас/", views.about, name="about"),
    path("производство/", views.manufacturing_page, name="manufacturing"),
    path("партнёры/", views.partners_page, name="partners"),
    path("галерея/", views.gallery_page, name="gallery"),
    path("продукция/", views.product_list, name="products"),
    path("продукция/<int:pk>/", views.product_detail, name="product_detail"),
    path('новости/', views.news_page, name='news'),
    path('новости/<int:id>/', views.news_detail, name='news_detail'),
]
