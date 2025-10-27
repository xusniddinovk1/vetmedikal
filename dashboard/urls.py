from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('kirish/', views.login_page, name='login_page'),
    path('chiqish/', views.logout_page, name='logout_page'),

    path('profilim/', views.my_profile, name='my_profile'),
    path('profilim/tahrirlash/', views.profile_edit, name='profile_edit'),

    path('profil/parolni-almashtirish/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('profil/parol/ozgardi/', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='password_change_done'),

    path('umumiy-malumot/', views.manufacturing_overview_list, name='overview_list'),
    path('umumiy-malumot/yangi/', views.manufacturing_overview_create, name='overview_create'),
    path('umumiy-malumot/<int:id>/tahrirlash/', views.manufacturing_overview_edit, name='overview_edit'),
    path('umumiy-malumot/<int:id>/ochirish/', views.manufacturing_overview_delete, name='overview_delete'),

    path('statistika/', views.manufacturing_stat_list, name='stat_list'),
    path('statistika/yangi/', views.manufacturing_stat_create, name='stat_create'),
    path('statistika/<int:id>/tahrirlash/', views.manufacturing_stat_edit, name='stat_edit'),
    path('statistika/<int:id>/ochirish/', views.manufacturing_stat_delete, name='stat_delete'),

    path('ishlab-chiqarish-qatori/', views.production_line_list, name='line_list'),
    path('ishlab-chiqarish-qatori/yangi/', views.production_line_create, name='line_create'),
    path('ishlab-chiqarish-qatori/<int:id>/tahrirlash/', views.production_line_edit, name='line_edit'),
    path('ishlab-chiqarish-qatori/<int:id>/ochirish/', views.production_line_delete, name='line_delete'),

    path('hamkorlar/', views.partner_list, name='partner_list'),
    path('hamkorlar/yangi/', views.partner_create, name='partner_create'),
    path('hamkorlar/<int:id>/tahrirlash/', views.partner_edit, name='partner_edit'),
    path('hamkorlar/<int:id>/ochirish/', views.partner_delete, name='partner_delete'),

    path('hamkorlik-afzalliklari/', views.partnership_benefit_list, name='benefit_list'),
    path('hamkorlik-afzalliklari/yangi/', views.partnership_benefit_create, name='benefit_create'),
    path('hamkorlik-afzalliklari/<int:id>/tahrirlash/', views.partnership_benefit_edit, name='benefit_edit'),
    path('hamkorlik-afzalliklari/<int:id>/ochirish/', views.partnership_benefit_delete, name='benefit_delete'),

    path('galereya-turlari/', views.gallery_category_list, name='gallery_category_list'),
    path('galereya-turlari/yangi/', views.gallery_category_create, name='gallery_category_create'),
    path('galereya-turlari/<int:id>/tahrirlash/', views.gallery_category_edit, name='gallery_category_edit'),
    path('galereya-turlari/<int:id>/ochirish/', views.gallery_category_delete, name='gallery_category_delete'),

    path('galereya/', views.gallery_list, name='gallery_list'),
    path('galereya/yangi/', views.gallery_create, name='gallery_create'),
    path('galereya/<int:id>/tahrirlash/', views.gallery_edit, name='gallery_edit'),
    path('galereya/<int:id>/ochirish/', views.gallery_delete, name='gallery_delete'),

    path('kategoriyalar/', views.category_list, name='category_list'),
    path('kategoriyalar/yangi/', views.category_create, name='category_create'),
    path('kategoriyalar/<int:id>/tahrirlash/', views.category_edit, name='category_edit'),
    path('kategoriyalar/<int:id>/ochirish/', views.category_delete, name='category_delete'),

    path('yangiliklar/', views.news_list, name='news_list'),
    path('yangiliklar/yangi/', views.news_create, name='news_create'),
    path('yangiliklar/<int:id>/tahrirlash/', views.news_edit, name='news_edit'),
    path('yangiliklar/<int:id>/ochirish/', views.news_delete, name='news_delete'),

    path("mahsulot-turlari/", views.product_category_list, name="product_category_list"),
    path("mahsulot-turlari/yangi/", views.product_category_create, name="product_category_create"),
    path("mahsulot-turlari/<int:id>/tahrirlash/", views.product_category_edit, name="product_category_edit"),
    path("mahsulot-turlari/<int:id>/ochirish/", views.product_category_delete, name="product_category_delete"),

    path("mahsulotlar/", views.product_list, name="product_list"),
    path("mahsulotlar/yangi/", views.product_create, name="product_create"),
    path("mahsulotlar/<int:id>/tahrirlash/", views.product_edit, name="product_edit"),
    path("mahsulotlar/<int:id>/ochirish/", views.product_delete, name="product_delete"),

    path("xususiyatlar/", views.feature_list, name="feature_list"),
    path("xususiyatlar/yangi/", views.feature_create, name="feature_create"),
    path("xususiyatlar/<int:id>/tahrirlash/", views.feature_edit, name="feature_edit"),
    path("xususiyatlar/<int:id>/ochirish/", views.feature_delete, name="feature_delete"),

    path("rasmlar/", views.image_list, name="image_list"),
    path("rasmlar/yangi/", views.image_create, name="image_create"),
    path("rasmlar/<int:id>/tahrirlash/", views.image_edit, name="image_edit"),
    path("rasmlar/<int:id>/ochirish/", views.image_delete, name="image_delete"),

    path("xizmatlar/", views.service_list, name="service_list"),
    path("xizmatlar/yangi/", views.service_create, name="service_create"),
    path("xizmatlar/<int:id>/tahrirlash/", views.service_edit, name="service_edit"),
    path("xizmatlar/<int:id>/ochirish/", views.service_delete, name="service_delete"),

    path("mahsulot-xususiyatlari/", views.product_feature_list, name="product_feature_list"),
    path("mahsulot-xususiyatlari/yangi/", views.product_feature_create, name="product_feature_create"),
    path("mahsulot-xususiyatlari/<int:id>/tahrirlash/", views.product_feature_edit, name="product_feature_edit"),
    path("mahsulot-xususiyatlari/<int:id>/ochirish/", views.product_feature_delete, name="product_feature_delete"),

    path("kontaktlar/", views.contact_list, name="contact_list"),
    path("kontaktlar/yangi/", views.contact_create, name="contact_create"),
    path("kontaktlar/<int:id>/tahrirlash/", views.contact_edit, name="contact_edit"),
    path("kontaktlar/<int:id>/ochirish/", views.contact_delete, name="contact_delete"),

    path("internet/", views.internet_list, name="internet_list"),
    path("internet/yangi/", views.internet_create, name="internet_create"),
    path("internet/<int:id>/tahrirlash/", views.internet_edit, name="internet_edit"),
    path("internet/<int:id>/ochirish/", views.internet_delete, name="internet_delete"),

    path("missiya/", views.mission_list, name="mission_list"),
    path("missiya/yangi/", views.mission_create, name="mission_create"),
    path("missiya/<int:id>/tahrirlash/", views.mission_edit, name="mission_edit"),
    path("missiya/<int:id>/ochirish/", views.mission_delete, name="mission_delete"),

    path("missiya-punktlari/", views.mission_point_list, name="mission_point_list"),
    path("missiya-punktlari/yangi/", views.mission_point_create, name="mission_point_create"),
    path("missiya-punktlari/<int:id>/tahrirlash/", views.mission_point_edit, name="mission_point_edit"),
    path("missiya-punktlari/<int:id>/ochirish/", views.mission_point_delete, name="mission_point_delete"),

    path("statistikalar/", views.statistic_list, name="statistic_list"),
    path("statistikalar/yangi/", views.statistic_create, name="statistic_create"),
    path("statistikalar/<int:id>/tahrirlash/", views.statistic_edit, name="statistic_edit"),
    path("statistikalar/<int:id>/ochirish/", views.statistic_delete, name="statistic_delete"),

    path("qadriyatlar/", views.value_list, name="value_list"),
    path("qadriyatlar/yangi/", views.value_create, name="value_create"),
    path("qadriyatlar/<int:id>/tahrirlash/", views.value_edit, name="value_edit"),
    path("qadriyatlar/<int:id>/ochirish/", views.value_delete, name="value_delete"),

    path("yutuqlar/", views.achievement_list, name="achievement_list"),
    path("yutuqlar/yangi/", views.achievement_create, name="achievement_create"),
    path("yutuqlar/<int:id>/tahrirlash/", views.achievement_edit, name="achievement_edit"),
    path("yutuqlar/<int:id>/ochirish/", views.achievement_delete, name="achievement_delete"),

    path("jamoa-azolari/", views.member_list, name="member_list"),
    path("jamoa-azolari/yangi/", views.member_create, name="member_create"),
    path("jamoa-azolari/<int:id>/tahrirlash/", views.member_edit, name="member_edit"),
    path("jamoa-azolari/<int:id>/ochirish/", views.member_delete, name="member_delete"),

    path("tarixlar/", views.history_list, name="history_list"),
    path("tarixlar/yangi/", views.history_create, name="history_create"),
    path("tarixlar/<int:id>/tahrirlash/", views.history_edit, name="history_edit"),
    path("tarixlar/<int:id>/ochirish/", views.history_delete, name="history_delete"),
]
