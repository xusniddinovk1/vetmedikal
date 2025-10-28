from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('kirish/', views.login_page, name='login'),
    path('chiqish/', views.logout_page, name='logout'),

    path('profilim/', views.my_profile, name='mening_profilim'),
    path('profilim/tahrirlash/', views.profile_edit, name='mening_profilim_tahrirlash'),

    path('profil/parolni-almashtirish/', views.CustomPasswordChangeView.as_view(), name='parol_almashtirish'),
    path('profil/parol/ozgardi/', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='parol_ozgartirildi'),

    path('umumiy-malumot/', views.manufacturing_overview_list, name='umumiy_list'),
    path('umumiy-malumot/yangi/', views.manufacturing_overview_create, name='umumiy_create'),
    path('umumiy-malumot/<int:id>/tahrirlash/', views.manufacturing_overview_edit, name='umumiy_edit'),
    path('umumiy-malumot/<int:id>/ochirish/', views.manufacturing_overview_delete, name='umumiy_delete'),

    path('statistika/', views.manufacturing_stat_list, name='statistika_list'),
    path('statistika/yangi/', views.manufacturing_stat_create, name='statistika_create'),
    path('statistika/<int:id>/tahrirlash/', views.manufacturing_stat_edit, name='statistika_edit'),
    path('statistika/<int:id>/ochirish/', views.manufacturing_stat_delete, name='statistika_delete'),

    path('ishlab-chiqarish-qatori/', views.production_line_list, name='qator_list'),
    path('ishlab-chiqarish-qatori/yangi/', views.production_line_create, name='qator_create'),
    path('ishlab-chiqarish-qatori/<int:id>/tahrirlash/', views.production_line_edit, name='qator_edit'),
    path('ishlab-chiqarish-qatori/<int:id>/ochirish/', views.production_line_delete, name='qator_delete'),

    path('hamkorlar/', views.partner_list, name='hamkor_list'),
    path('hamkorlar/yangi/', views.partner_create, name='hamkor_create'),
    path('hamkorlar/<int:id>/tahrirlash/', views.partner_edit, name='hamkor_edit'),
    path('hamkorlar/<int:id>/ochirish/', views.partner_delete, name='hamkor_delete'),

    path('hamkorlik-afzalliklari/', views.partnership_benefit_list, name='afzallik_list'),
    path('hamkorlik-afzalliklari/yangi/', views.partnership_benefit_create, name='afzallik_create'),
    path('hamkorlik-afzalliklari/<int:id>/tahrirlash/', views.partnership_benefit_edit, name='afzallik_edit'),
    path('hamkorlik-afzalliklari/<int:id>/ochirish/', views.partnership_benefit_delete, name='afzallik_delete'),

    path('galereya-turlari/', views.gallery_category_list, name='rasm_tur_list'),
    path('galereya-turlari/yangi/', views.gallery_category_create, name='rasm_tur_create'),
    path('galereya-turlari/<int:id>/tahrirlash/', views.gallery_category_edit, name='rasm_tur_edit'),
    path('galereya-turlari/<int:id>/ochirish/', views.gallery_category_delete, name='rasm_tur_delete'),

    path('galereya/', views.gallery_list, name='galereya_list'),
    path('galereya/yangi/', views.gallery_create, name='galereya_create'),
    path('galereya/<int:id>/tahrirlash/', views.gallery_edit, name='galereya_edit'),
    path('galereya/<int:id>/ochirish/', views.gallery_delete, name='galereya_delete'),

    path('kategoriyalar/', views.category_list, name='kateg_list'),
    path('kategoriyalar/yangi/', views.category_create, name='kateg_create'),
    path('kategoriyalar/<int:id>/tahrirlash/', views.category_edit, name='kateg_edit'),
    path('kategoriyalar/<int:id>/ochirish/', views.category_delete, name='kateg_delete'),

    path('yangiliklar/', views.news_list, name='yangi_list'),
    path('yangiliklar/yangi/', views.news_create, name='yangi_create'),
    path('yangiliklar/<int:id>/tahrirlash/', views.news_edit, name='yangi_edit'),
    path('yangiliklar/<int:id>/ochirish/', views.news_delete, name='yangi_delete'),

    path("mahsulot-turlari/", views.product_category_list, name="mah_kat_list"),
    path("mahsulot-turlari/yangi/", views.product_category_create, name="mah_kat_create"),
    path("mahsulot-turlari/<int:id>/tahrirlash/", views.product_category_edit, name="mah_kat_edit"),
    path("mahsulot-turlari/<int:id>/ochirish/", views.product_category_delete, name="mah_kat_delete"),

    path("mahsulotlar/", views.product_list, name="mahsulot_list"),
    path("mahsulotlar/yangi/", views.product_create, name="mahsulot_create"),
    path("mahsulotlar/<int:id>/tahrirlash/", views.product_edit, name="mahsulot_edit"),
    path("mahsulotlar/<int:id>/ochirish/", views.product_delete, name="mahsulot_delete"),

    path("xususiyatlar/", views.feature_list, name="xusus_list"),
    path("xususiyatlar/yangi/", views.feature_create, name="xusus_create"),
    path("xususiyatlar/<int:id>/tahrirlash/", views.feature_edit, name="xusus_edit"),
    path("xususiyatlar/<int:id>/ochirish/", views.feature_delete, name="xusus_delete"),

    path("rasmlar/", views.image_list, name="rasmlar_list"),
    path("rasmlar/yangi/", views.image_create, name="rasmlar_create"),
    path("rasmlar/<int:id>/tahrirlash/", views.image_edit, name="rasmlar_edit"),
    path("rasmlar/<int:id>/ochirish/", views.image_delete, name="rasmlar_delete"),

    path("xizmatlar/", views.service_list, name="xizmatlar_list"),
    path("xizmatlar/yangi/", views.service_create, name="xizmatlar_create"),
    path("xizmatlar/<int:id>/tahrirlash/", views.service_edit, name="xizmatlar_edit"),
    path("xizmatlar/<int:id>/ochirish/", views.service_delete, name="xizmatlar_delete"),

    path("mahsulot-xususiyatlari/", views.product_feature_list, name="mahsulot_xusus_list"),
    path("mahsulot-xususiyatlari/yangi/", views.product_feature_create, name="mahsulot_xusus_create"),
    path("mahsulot-xususiyatlari/<int:id>/tahrirlash/", views.product_feature_edit, name="mahsulot_xusus_edit"),
    path("mahsulot-xususiyatlari/<int:id>/ochirish/", views.product_feature_delete, name="mahsulot_xusus_delete"),

    path("kontaktlar/", views.contact_list, name="kontaktlar_list"),
    path("kontaktlar/yangi/", views.contact_create, name="kontaktlar_create"),
    path("kontaktlar/<int:id>/tahrirlash/", views.contact_edit, name="kontaktlar_edit"),
    path("kontaktlar/<int:id>/ochirish/", views.contact_delete, name="kontaktlar_delete"),

    path("internet/", views.internet_list, name="tarmoqlar_list"),
    path("internet/yangi/", views.internet_create, name="tarmoqlar_create"),
    path("internet/<int:id>/tahrirlash/", views.internet_edit, name="tarmoqlar_edit"),
    path("internet/<int:id>/ochirish/", views.internet_delete, name="tarmoqlar_delete"),

    path("missiya/", views.mission_list, name="missiya_list"),
    path("missiya/yangi/", views.mission_create, name="missiya_create"),
    path("missiya/<int:id>/tahrirlash/", views.mission_edit, name="missiya_edit"),
    path("missiya/<int:id>/ochirish/", views.mission_delete, name="missiya_delete"),

    path("missiya-punktlari/", views.mission_point_list, name="missiya_punkt_list"),
    path("missiya-punktlari/yangi/", views.mission_point_create, name="missiya_punkt_create"),
    path("missiya-punktlari/<int:id>/tahrirlash/", views.mission_point_edit, name="missiya_punkt_edit"),
    path("missiya-punktlari/<int:id>/ochirish/", views.mission_point_delete, name="missiya_punkt_delete"),

    path("statistikalar/", views.statistic_list, name="statlar_list"),
    path("statistikalar/yangi/", views.statistic_create, name="statlar_create"),
    path("statistikalar/<int:id>/tahrirlash/", views.statistic_edit, name="statlar_edit"),
    path("statistikalar/<int:id>/ochirish/", views.statistic_delete, name="statlar_delete"),

    path("qadriyatlar/", views.value_list, name="qadriyatlar_list"),
    path("qadriyatlar/yangi/", views.value_create, name="qadriyatlar_create"),
    path("qadriyatlar/<int:id>/tahrirlash/", views.value_edit, name="qadriyatlar_edit"),
    path("qadriyatlar/<int:id>/ochirish/", views.value_delete, name="qadriyatlar_delete"),

    path("yutuqlar/", views.achievement_list, name="yutuqlar_list"),
    path("yutuqlar/yangi/", views.achievement_create, name="yutuqlar_create"),
    path("yutuqlar/<int:id>/tahrirlash/", views.achievement_edit, name="yutuqlar_edit"),
    path("yutuqlar/<int:id>/ochirish/", views.achievement_delete, name="yutuqlar_delete"),

    path("jamoa-azolari/", views.member_list, name="azolar_list"),
    path("jamoa-azolari/yangi/", views.member_create, name="azolar_create"),
    path("jamoa-azolari/<int:id>/tahrirlash/", views.member_edit, name="azolar_edit"),
    path("jamoa-azolari/<int:id>/ochirish/", views.member_delete, name="azolar_delete"),

    path("tarixlar/", views.history_list, name="tarix_list"),
    path("tarixlar/yangi/", views.history_create, name="tarix_create"),
    path("tarixlar/<int:id>/tahrirlash/", views.history_edit, name="tarix_edit"),
    path("tarixlar/<int:id>/ochirish/", views.history_delete, name="tarix_delete"),
]
