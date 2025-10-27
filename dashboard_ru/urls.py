from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard_ru'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('логин/', views.login_page, name='login_page'),
    path('логоут/', views.logout_page, name='logout_page'),

    path('мой-профиль/', views.my_profile, name='my_profile'),
    path('мой-профиль/редактировать/', views.profile_edit, name='profile_edit'),

    path('профиль/сменить-пароль/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('профиль/пароль/готово/', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='password_change_done'),

    path('обзор/', views.manufacturing_overview_list, name='overview_list'),
    path('обзор/создать/', views.manufacturing_overview_create, name='overview_create'),
    path('обзор/<int:id>/редактировать/', views.manufacturing_overview_edit, name='overview_edit'),
    path('обзор/<int:id>/удалить/', views.manufacturing_overview_delete, name='overview_delete'),

    path('статистика-производства/', views.manufacturing_stat_list, name='stat_list'),
    path('статистика-производства/создать/', views.manufacturing_stat_create, name='stat_create'),
    path('статистика-производства/<int:id>/редактировать/', views.manufacturing_stat_edit, name='stat_edit'),
    path('статистика-производства/<int:id>/удалить/', views.manufacturing_stat_delete, name='stat_delete'),

    path('производственная-линия/', views.production_line_list, name='line_list'),
    path('производственная-линия/создать/', views.production_line_create, name='line_create'),
    path('производственная-линия/<int:id>/редактировать/', views.production_line_edit, name='line_edit'),
    path('производственная-линия/<int:id>/удалить/', views.production_line_delete, name='line_delete'),

    path('партнеры/', views.partner_list, name='partner_list'),
    path('партнеры/создать/', views.partner_create, name='partner_create'),
    path('партнеры/<int:id>/редактировать/', views.partner_edit, name='partner_edit'),
    path('партнеры/<int:id>/удалить/', views.partner_delete, name='partner_delete'),

    path('преимущества-партнерства/', views.partnership_benefit_list, name='benefit_list'),
    path('преимущества-партнерства/создать/', views.partnership_benefit_create, name='benefit_create'),
    path('преимущества-партнерства/<int:id>/редактировать/', views.partnership_benefit_edit, name='benefit_edit'),
    path('преимущества-партнерства/<int:id>/удалить/', views.partnership_benefit_delete, name='benefit_delete'),

    path('категории-галереи/', views.gallery_category_list, name='gallery_category_list'),
    path('категории-галереи/создать/', views.gallery_category_create, name='gallery_category_create'),
    path('категории-галереи/<int:id>/редактировать/', views.gallery_category_edit, name='gallery_category_edit'),
    path('категории-галереи/<int:id>/удалить/', views.gallery_category_delete, name='gallery_category_delete'),

    path('галерея/', views.gallery_list, name='gallery_list'),
    path('галерея/создать/', views.gallery_create, name='gallery_create'),
    path('галерея/<int:id>/редактировать/', views.gallery_edit, name='gallery_edit'),
    path('галерея/<int:id>/удалить/', views.gallery_delete, name='gallery_delete'),

    path('категории/', views.category_list, name='category_list'),
    path('категории/создать/', views.category_create, name='category_create'),
    path('категории/<int:id>/редактировать/', views.category_edit, name='category_edit'),
    path('категории/<int:id>/удалить/', views.category_delete, name='category_delete'),

    path('новости/', views.news_list, name='news_list'),
    path('новости/создать/', views.news_create, name='news_create'),
    path('новости/<int:id>/редактировать/', views.news_edit, name='news_edit'),
    path('новости/<int:id>/удалить/', views.news_delete, name='news_delete'),

    path('категории-продуктов/', views.product_category_list, name='product_category_list'),
    path('категории-продуктов/создать/', views.product_category_create, name='product_category_create'),
    path('категории-продуктов/<int:id>/редактировать/', views.product_category_edit, name='product_category_edit'),
    path('категории-продуктов/<int:id>/удалить/', views.product_category_delete, name='product_category_delete'),

    path('продукты/', views.product_list, name='product_list'),
    path('продукты/создать/', views.product_create, name='product_create'),
    path('продукты/<int:id>/редактировать/', views.product_edit, name='product_edit'),
    path('продукты/<int:id>/удалить/', views.product_delete, name='product_delete'),

    path('особенности/', views.feature_list, name='feature_list'),
    path('особенности/создать/', views.feature_create, name='feature_create'),
    path('особенности/<int:id>/редактировать/', views.feature_edit, name='feature_edit'),
    path('особенности/<int:id>/удалить/', views.feature_delete, name='feature_delete'),

    path('изображения/', views.image_list, name='image_list'),
    path('изображения/создать/', views.image_create, name='image_create'),
    path('изображения/<int:id>/редактировать/', views.image_edit, name='image_edit'),
    path('изображения/<int:id>/удалить/', views.image_delete, name='image_delete'),

    path('услуги/', views.service_list, name='service_list'),
    path('услуги/создать/', views.service_create, name='service_create'),
    path('услуги/<int:id>/редактировать/', views.service_edit, name='service_edit'),
    path('услуги/<int:id>/удалить/', views.service_delete, name='service_delete'),

    path('характеристики-продуктов/', views.product_feature_list, name='product_feature_list'),
    path('характеристики-продуктов/создать/', views.product_feature_create, name='product_feature_create'),
    path('характеристики-продуктов/<int:id>/редактировать/', views.product_feature_edit, name='product_feature_edit'),
    path('характеристики-продуктов/<int:id>/удалить/', views.product_feature_delete, name='product_feature_delete'),

    path('контакты/', views.contact_list, name='contact_list'),
    path('контакты/создать/', views.contact_create, name='contact_create'),
    path('контакты/<int:id>/редактировать/', views.contact_edit, name='contact_edit'),
    path('контакты/<int:id>/удалить/', views.contact_delete, name='contact_delete'),

    path('интернет/', views.internet_list, name='internet_list'),
    path('интернет/создать/', views.internet_create, name='internet_create'),
    path('интернет/<int:id>/редактировать/', views.internet_edit, name='internet_edit'),
    path('интернет/<int:id>/удалить/', views.internet_delete, name='internet_delete'),

    path('миссия/', views.mission_list, name='mission_list'),
    path('миссия/создать/', views.mission_create, name='mission_create'),
    path('миссия/<int:id>/редактировать/', views.mission_edit, name='mission_edit'),
    path('миссия/<int:id>/удалить/', views.mission_delete, name='mission_delete'),

    path('пункты-миссии/', views.mission_point_list, name='mission_point_list'),
    path('пункты-миссии/создать/', views.mission_point_create, name='mission_point_create'),
    path('пункты-миссии/<int:id>/редактировать/', views.mission_point_edit, name='mission_point_edit'),
    path('пункты-миссии/<int:id>/удалить/', views.mission_point_delete, name='mission_point_delete'),

    path('статистика/', views.statistic_list, name='statistic_list'),
    path('статистика/создать/', views.statistic_create, name='statistic_create'),
    path('статистика/<int:id>/редактировать/', views.statistic_edit, name='statistic_edit'),
    path('статистика/<int:id>/удалить/', views.statistic_delete, name='statistic_delete'),

    path('ценности/', views.value_list, name='value_list'),
    path('ценности/создать/', views.value_create, name='value_create'),
    path('ценности/<int:id>/редактировать/', views.value_edit, name='value_edit'),
    path('ценности/<int:id>/удалить/', views.value_delete, name='value_delete'),

    path('достижения/', views.achievement_list, name='achievement_list'),
    path('достижения/создать/', views.achievement_create, name='achievement_create'),
    path('достижения/<int:id>/редактировать/', views.achievement_edit, name='achievement_edit'),
    path('достижения/<int:id>/удалить/', views.achievement_delete, name='achievement_delete'),

    path('члены-команды/', views.member_list, name='member_list'),
    path('члены-команды/создать/', views.member_create, name='member_create'),
    path('члены-команды/<int:id>/редактировать/', views.member_edit, name='member_edit'),
    path('члены-команды/<int:id>/удалить/', views.member_delete, name='member_delete'),

    path('история/', views.history_list, name='history_list'),
    path('история/создать/', views.history_create, name='history_create'),
    path('история/<int:id>/редактировать/', views.history_edit, name='history_edit'),
    path('история/<int:id>/удалить/', views.history_delete, name='history_delete'),
]
