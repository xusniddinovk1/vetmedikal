from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard_ru'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),

    path('my-profile', views.my_profile, name='my_profile', ),
    path('my-profile/edit/', views.profile_edit, name='profile_edit'),

    path('profile/change/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('profile/password/done', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='password_change_done'),

    path('overview/', views.manufacturing_overview_list, name='overview_list'),
    path('overview/create/', views.manufacturing_overview_create, name='overview_create'),
    path('overview/<int:id>/edit/', views.manufacturing_overview_edit, name='overview_edit'),
    path('overview/<int:id>/delete/', views.manufacturing_overview_delete, name='overview_delete'),

    path('stat/', views.manufacturing_stat_list, name='stat_list'),
    path('stat/create/', views.manufacturing_stat_create, name='stat_create'),
    path('stat/<int:id>/edit/', views.manufacturing_stat_edit, name='stat_edit'),
    path('stat/<int:id>/delete/', views.manufacturing_stat_delete, name='stat_delete'),

    path('line/', views.production_line_list, name='line_list'),
    path('line/create/', views.production_line_create, name='line_create'),
    path('line/<int:id>/edit/', views.production_line_edit, name='line_edit'),
    path('line/<int:id>/delete/', views.production_line_delete, name='line_delete'),

    path('partner/', views.partner_list, name='partner_list'),
    path('partner/create/', views.partner_create, name='partner_create'),
    path('partner/<int:id>/edit/', views.partner_edit, name='partner_edit'),
    path('partner/<int:id>/delete/', views.partner_delete, name='partner_delete'),

    path('benefit/', views.partnership_benefit_list, name='benefit_list'),
    path('benefit/create/', views.partnership_benefit_create, name='benefit_create'),
    path('benefit/<int:id>/edit/', views.partnership_benefit_edit, name='benefit_edit'),
    path('benefit/<int:id>/delete/', views.partnership_benefit_delete, name='benefit_delete'),

    path('gallery-category/', views.gallery_category_list, name='gallery_category_list'),
    path('gallery-category/create/', views.gallery_category_create, name='gallery_category_create'),
    path('gallery-category/<int:id>/edit/', views.gallery_category_edit, name='gallery_category_edit'),
    path('gallery-category/<int:id>/delete/', views.gallery_category_delete, name='gallery_category_delete'),

    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:id>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:id>/delete/', views.gallery_delete, name='gallery_delete'),

    path('category/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:id>/delete/', views.category_delete, name='category_delete'),

    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:id>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:id>/delete/', views.news_delete, name='news_delete'),

    path("categories/", views.product_category_list, name="product_category_list"),
    path("categories/create/", views.product_category_create, name="product_category_create"),
    path("categories/<int:id>/edit/", views.product_category_edit, name="product_category_edit"),
    path("categories/<int:id>/delete/", views.product_category_delete, name="product_category_delete"),

    path("products/", views.product_list, name="product_list"),
    path("products/create/", views.product_create, name="product_create"),
    path("products/<int:id>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:id>/delete/", views.product_delete, name="product_delete"),

    path("features/", views.feature_list, name="feature_list"),
    path("features/create/", views.feature_create, name="feature_create"),
    path("features/<int:id>/edit/", views.feature_edit, name="feature_edit"),
    path("features/<int:id>/delete/", views.feature_delete, name="feature_delete"),

    path("images/", views.image_list, name="image_list"),
    path("images/create/", views.image_create, name="image_create"),
    path("images/<int:id>/edit/", views.image_edit, name="image_edit"),
    path("images/<int:id>/delete/", views.image_delete, name="image_delete"),

    path("services/", views.service_list, name="service_list"),
    path("services/create/", views.service_create, name="service_create"),
    path("services/<int:id>/edit/", views.service_edit, name="service_edit"),
    path("services/<int:id>/delete/", views.service_delete, name="service_delete"),

    path("product-features/", views.product_feature_list, name="product_feature_list"),
    path("product-features/create/", views.product_feature_create, name="product_feature_create"),
    path("product-features/<int:id>/edit/", views.product_feature_edit, name="product_feature_edit"),
    path("product-features/<int:id>/delete/", views.product_feature_delete, name="product_feature_delete"),

    path("contacts/", views.contact_list, name="contact_list"),
    path("contacts/create/", views.contact_create, name="contact_create"),
    path("contacts/<int:id>/edit/", views.contact_edit, name="contact_edit"),
    path("contacts/<int:id>/delete/", views.contact_delete, name="contact_delete"),

    path("internet/", views.internet_list, name="internet_list"),
    path("internet/create/", views.internet_create, name="internet_create"),
    path("internet/<int:id>/edit/", views.internet_edit, name="internet_edit"),
    path("internet/<int:id>/delete/", views.internet_delete, name="internet_delete"),

    path("missions/", views.mission_list, name="mission_list"),
    path("missions/create/", views.mission_create, name="mission_create"),
    path("missions/<int:id>/edit/", views.mission_edit, name="mission_edit"),
    path("missions/<int:id>/delete/", views.mission_delete, name="mission_delete"),

    path("mission-points/", views.mission_point_list, name="mission_point_list"),
    path("mission-points/create/", views.mission_point_create, name="mission_point_create"),
    path("mission-points/<int:id>/edit/", views.mission_point_edit, name="mission_point_edit"),
    path("mission-points/<int:id>/delete/", views.mission_point_delete, name="mission_point_delete"),

    path("statistics/", views.statistic_list, name="statistic_list"),
    path("statistics/create/", views.statistic_create, name="statistic_create"),
    path("statistics/<int:id>/edit/", views.statistic_edit, name="statistic_edit"),
    path("statistics/<int:id>/delete/", views.statistic_delete, name="statistic_delete"),

    path("values/", views.value_list, name="value_list"),
    path("values/create/", views.value_create, name="value_create"),
    path("values/<int:id>/edit/", views.value_edit, name="value_edit"),
    path("values/<int:id>/delete/", views.value_delete, name="value_delete"),

    path("achievements/", views.achievement_list, name="achievement_list"),
    path("achievements/create/", views.achievement_create, name="achievement_create"),
    path("achievements/<int:id>/edit/", views.achievement_edit, name="achievement_edit"),
    path("achievements/<int:id>/delete/", views.achievement_delete, name="achievement_delete"),

    path("members/", views.member_list, name="member_list"),
    path("members/create/", views.member_create, name="member_create"),
    path("members/<int:id>/edit/", views.member_edit, name="member_edit"),
    path("members/<int:id>/delete/", views.member_delete, name="member_delete"),

    path("histories/", views.history_list, name="history_list"),
    path("histories/create/", views.history_create, name="history_create"),
    path("histories/<int:id>/edit/", views.history_edit, name="history_edit"),
    path("histories/<int:id>/delete/", views.history_delete, name="history_delete"),
]
