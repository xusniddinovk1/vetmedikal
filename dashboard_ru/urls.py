from django.urls import path
from dashboard_ru.views import *
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard_ru'

urlpatterns = [
    path('', home_page, name='glavnaya_stranitsa'),
    path('логин/', login_page, name='vhod_stranitsa'),
    path('логоут/', logout_page, name='vyhod_stranitsa'),

    path('мой-профиль/', my_profile, name='moy_profil'),
    path('мой-профиль/редактировать/', profile_edit, name='redaktirovat_profil'),

    path('профиль/сменить-пароль/', CustomPasswordChangeView.as_view(), name='smena_parolya'),
    path('профиль/пароль/готово/', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='parol_izmenen'),

    path('обзор/', manufacturing_overview_list, name='obzor_spisok'),
    path('обзор/создать/', manufacturing_overview_create, name='obzor_sozdat'),
    path('обзор/<int:id>/редактировать/', manufacturing_overview_edit, name='obzor_redaktirovat'),
    path('обзор/<int:id>/удалить/', manufacturing_overview_delete, name='obzor_udalit'),

    path('статистика-производства/', manufacturing_stat_list, name='statistika_proizvodstva_spisok'),
    path('статистика-производства/создать/', manufacturing_stat_create, name='statistika_proizvodstva_sozdat'),
    path('статистика-производства/<int:id>/редактировать/', manufacturing_stat_edit,
         name='statistika_proizvodstva_redaktirovat'),
    path('статистика-производства/<int:id>/удалить/', manufacturing_stat_delete, name='statistika_proizvodstva_udalit'),

    path('производственная-линия/', production_line_list, name='proizvodstvennaya_liniya_spisok'),
    path('производственная-линия/создать/', production_line_create, name='proizvodstvennaya_liniya_sozdat'),
    path('производственная-линия/<int:id>/редактировать/', production_line_edit,
         name='proizvodstvennaya_liniya_redaktirovat'),
    path('производственная-линия/<int:id>/удалить/', production_line_delete, name='proizvodstvennaya_liniya_udalit'),

    path('партнеры/', partner_list, name='partnery_spisok'),
    path('партнеры/создать/', partner_create, name='partnery_sozdat'),
    path('партнеры/<int:id>/редактировать/', partner_edit, name='partnery_redaktirovat'),
    path('партнеры/<int:id>/удалить/', partner_delete, name='partnery_udalit'),

    path('преимущества-партнерства/', partnership_benefit_list, name='preimushchestva_partnyorstva_spisok'),
    path('преимущества-партнерства/создать/', partnership_benefit_create, name='preimushchestva_partnyorstva_sozdat'),
    path('преимущества-партнерства/<int:id>/редактировать/', partnership_benefit_edit,
         name='preimushchestva_partnyorstva_redaktirovat'),
    path('преимущества-партнерства/<int:id>/удалить/', partnership_benefit_delete,
         name='preimushchestva_partnyorstva_udalit'),

    path('категории-галереи/', gallery_category_list, name='kategoriya_galerei_spisok'),
    path('категории-галереи/создать/', gallery_category_create, name='kategoriya_galerei_sozdat'),
    path('категории-галереи/<int:id>/редактировать/', gallery_category_edit, name='kategoriya_galerei_redaktirovat'),
    path('категории-галереи/<int:id>/удалить/', gallery_category_delete, name='kategoriya_galerei_udalit'),

    path('галерея/', gallery_list, name='galereya_spisok'),
    path('галерея/создать/', gallery_create, name='galereya_sozdat'),
    path('галерея/<int:id>/редактировать/', gallery_edit, name='galereya_redaktirovat'),
    path('галерея/<int:id>/удалить/', gallery_delete, name='galereya_udalit'),

    path('категории/', category_list, name='kategoriya_spisok'),
    path('категории/создать/', category_create, name='kategoriya_sozdat'),
    path('категории/<int:id>/редактировать/', category_edit, name='kategoriya_redaktirovat'),
    path('категории/<int:id>/удалить/', category_delete, name='kategoriya_udalit'),

    path('новости/', news_list, name='novosti_spisok'),
    path('новости/создать/', news_create, name='novosti_sozdat'),
    path('новости/<int:id>/редактировать/', news_edit, name='novosti_redaktirovat'),
    path('новости/<int:id>/удалить/', news_delete, name='novosti_udalit'),

    path('категории-продуктов/', product_category_list, name='kategoriya_produktov_spisok'),
    path('категории-продуктов/создать/', product_category_create, name='kategoriya_produktov_sozdat'),
    path('категории-продуктов/<int:id>/редактировать/', product_category_edit,
         name='kategoriya_produktov_redaktirovat'),
    path('категории-продуктов/<int:id>/удалить/', product_category_delete, name='kategoriya_produktov_udalit'),

    path('продукты/', product_list, name='produkty_spisok'),
    path('продукты/создать/', product_create, name='produkty_sozdat'),
    path('продукты/<int:id>/редактировать/', product_edit, name='produkty_redaktirovat'),
    path('продукты/<int:id>/удалить/', product_delete, name='produkty_udalit'),

    path('особенности/', feature_list, name='osobennosti_spisok'),
    path('особенности/создать/', feature_create, name='osobennosti_sozdat'),
    path('особенности/<int:id>/редактировать/', feature_edit, name='osobennosti_redaktirovat'),
    path('особенности/<int:id>/удалить/', feature_delete, name='osobennosti_udalit'),

    path('изображения/', image_list, name='izobrazheniya_spisok'),
    path('изображения/создать/', image_create, name='izobrazheniya_sozdat'),
    path('изображения/<int:id>/редактировать/', image_edit, name='izobrazheniya_redaktirovat'),
    path('изображения/<int:id>/удалить/', image_delete, name='izobrazheniya_udalit'),

    path('услуги/', service_list, name='uslugi_spisok'),
    path('услуги/создать/', service_create, name='uslugi_sozdat'),
    path('услуги/<int:id>/редактировать/', service_edit, name='uslugi_redaktirovat'),
    path('услуги/<int:id>/удалить/', service_delete, name='uslugi_udalit'),

    path('характеристики-продуктов/', product_feature_list, name='harakteristiki_produktov_spisok'),
    path('характеристики-продуктов/создать/', product_feature_create, name='harakteristiki_produktov_sozdat'),
    path('характеристики-продуктов/<int:id>/редактировать/', product_feature_edit,
         name='harakteristiki_produktov_redaktirovat'),
    path('характеристики-продуктов/<int:id>/удалить/', product_feature_delete, name='harakteristiki_produktov_udalit'),

    path('контакты/', contact_list, name='kontakty_spisok'),
    path('контакты/создать/', contact_create, name='kontakty_sozdat'),
    path('контакты/<int:id>/редактировать/', contact_edit, name='kontakty_redaktirovat'),
    path('контакты/<int:id>/удалить/', contact_delete, name='kontakty_udalit'),

    path('интернет/', internet_list, name='internet_spisok'),
    path('интернет/создать/', internet_create, name='internet_sozdat'),
    path('интернет/<int:id>/редактировать/', internet_edit, name='internet_redaktirovat'),
    path('интернет/<int:id>/удалить/', internet_delete, name='internet_udalit'),

    path('миссия/', mission_list, name='missiya_spisok'),
    path('миссия/создать/', mission_create, name='missiya_sozdat'),
    path('миссия/<int:id>/редактировать/', mission_edit, name='missiya_redaktirovat'),
    path('миссия/<int:id>/удалить/', mission_delete, name='missiya_udalit'),

    path('пункты-миссии/', mission_point_list, name='punkty_missii_spisok'),
    path('пункты-миссии/создать/', mission_point_create, name='punkty_missii_sozdat'),
    path('пункты-миссии/<int:id>/редактировать/', mission_point_edit, name='punkty_missii_redaktirovat'),
    path('пункты-миссии/<int:id>/удалить/', mission_point_delete, name='punkty_missii_udalit'),

    path('статистика/', statistic_list, name='statistika_spisok'),
    path('статистика/создать/', statistic_create, name='statistika_sozdat'),
    path('статистика/<int:id>/редактировать/', statistic_edit, name='statistika_redaktirovat'),
    path('статистика/<int:id>/удалить/', statistic_delete, name='statistika_udalit'),

    path('ценности/', value_list, name='tsennosti_spisok'),
    path('ценности/создать/', value_create, name='tsennosti_sozdat'),
    path('ценности/<int:id>/редактировать/', value_edit, name='tsennosti_redaktirovat'),
    path('ценности/<int:id>/удалить/', value_delete, name='tsennosti_udalit'),

    path('достижения/', achievement_list, name='dostizheniya_spisok'),
    path('достижения/создать/', achievement_create, name='dostizheniya_sozdat'),
    path('достижения/<int:id>/редактировать/', achievement_edit, name='dostizheniya_redaktirovat'),
    path('достижения/<int:id>/удалить/', achievement_delete, name='dostizheniya_udalit'),

    path('члены-команды/', member_list, name='chleny_komandy_spisok'),
    path('члены-команды/создать/', member_create, name='chleny_komandy_sozdat'),
    path('члены-команды/<int:id>/редактировать/', member_edit, name='chleny_komandy_redaktirovat'),
    path('члены-команды/<int:id>/удалить/', member_delete, name='chleny_komandy_udalit'),

    path('история/', history_list, name='istoriya_spisok'),
    path('история/создать/', history_create, name='istoriya_sozdat'),
    path('история/<int:id>/редактировать/', history_edit, name='istoriya_redaktirovat'),
    path('история/<int:id>/удалить/', history_delete, name='istoriya_udalit'),
]
