from django.urls import path
from dashboard_en import views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'dashboard_en'

urlpatterns = [
    path('', views.home_page1, name='home_page'),
    path('login/', views.login_page1, name='login_page'),
    path('logout/', views.logout_page1, name='logout_page'),

    path('my-profile', views.my_profile1, name='my_profile', ),
    path('my-profile/edit/', views.profile_edit1, name='profile_edit'),

    path('profile/change/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('profile/password/done', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='password_change_done'),

    path('overview/', views.manufacturing_overview_list1, name='overview_list'),
    path('overview/create/', views.manufacturing_overview_create1, name='overview_create'),
    path('overview/<int:id>/edit/', views.manufacturing_overview_edit1, name='overview_edit'),
    path('overview/<int:id>/delete/', views.manufacturing_overview_delete1, name='overview_delete'),

    path('stat/', views.manufacturing_stat_list1, name='stat_list'),
    path('stat/create/', views.manufacturing_stat_create1, name='stat_create'),
    path('stat/<int:id>/edit/', views.manufacturing_stat_edit1, name='stat_edit'),
    path('stat/<int:id>/delete/', views.manufacturing_stat_delete1, name='stat_delete'),

    path('line/', views.production_line_list1, name='line_list'),
    path('line/create/', views.production_line_create1, name='line_create'),
    path('line/<int:id>/edit/', views.production_line_edit1, name='line_edit'),
    path('line/<int:id>/delete/', views.production_line_delete1, name='line_delete'),

    path('partner/', views.partner_list1, name='partner_list'),
    path('partner/create/', views.partner_create1, name='partner_create'),
    path('partner/<int:id>/edit/', views.partner_edit1, name='partner_edit'),
    path('partner/<int:id>/delete/', views.partner_delete1, name='partner_delete'),

    path('benefit/', views.partnership_benefit_list1, name='benefit_list'),
    path('benefit/create/', views.partnership_benefit_create1, name='benefit_create'),
    path('benefit/<int:id>/edit/', views.partnership_benefit_edit1, name='benefit_edit'),
    path('benefit/<int:id>/delete/', views.partnership_benefit_delete1, name='benefit_delete'),

    path('gallery-category/', views.gallery_category_list1, name='gallery_category_list'),
    path('gallery-category/create/', views.gallery_category_create1, name='gallery_category_create'),
    path('gallery-category/<int:id>/edit/', views.gallery_category_edit1, name='gallery_category_edit'),
    path('gallery-category/<int:id>/delete/', views.gallery_category_delete1, name='gallery_category_delete'),

    path('gallery/', views.gallery_list1, name='gallery_list'),
    path('gallery/create/', views.gallery_create1, name='gallery_create'),
    path('gallery/<int:id>/edit/', views.gallery_edit1, name='gallery_edit'),
    path('gallery/<int:id>/delete/', views.gallery_delete1, name='gallery_delete'),

    path('category/', views.category_list1, name='category_list'),
    path('category/create/', views.category_create1, name='category_create'),
    path('category/<int:id>/edit/', views.category_edit1, name='category_edit'),
    path('category/<int:id>/delete/', views.category_delete1, name='category_delete'),

    path('news/', views.news_list1, name='news_list'),
    path('news/create/', views.news_create1, name='news_create'),
    path('news/<int:id>/edit/', views.news_edit1, name='news_edit'),
    path('news/<int:id>/delete/', views.news_delete1, name='news_delete'),

    path("categories/", views.product_category_list1, name="product_category_list"),
    path("categories/create/", views.product_category_create1, name="product_category_create"),
    path("categories/<int:id>/edit/", views.product_category_edit1, name="product_category_edit"),
    path("categories/<int:id>/delete/", views.product_category_delete1, name="product_category_delete"),

    path("products/", views.product_list1, name="product_list"),
    path("products/create/", views.product_create1, name="product_create"),
    path("products/<int:id>/edit/", views.product_edit1, name="product_edit"),
    path("products/<int:id>/delete/", views.product_delete1, name="product_delete"),

    path("features/", views.feature_list1, name="feature_list"),
    path("features/create/", views.feature_create1, name="feature_create"),
    path("features/<int:id>/edit/", views.feature_edit1, name="feature_edit"),
    path("features/<int:id>/delete/", views.feature_delete1, name="feature_delete"),

    path("images/", views.image_list1, name="image_list"),
    path("images/create/", views.image_create1, name="image_create"),
    path("images/<int:id>/edit/", views.image_edit1, name="image_edit"),
    path("images/<int:id>/delete/", views.image_delete1, name="image_delete"),

    path("services/", views.service_list1, name="service_list"),
    path("services/create/", views.service_create1, name="service_create"),
    path("services/<int:id>/edit/", views.service_edit1, name="service_edit"),
    path("services/<int:id>/delete/", views.service_delete1, name="service_delete"),

    path("product-features/", views.product_feature_list1, name="product_feature_list"),
    path("product-features/create/", views.product_feature_create1, name="product_feature_create"),
    path("product-features/<int:id>/edit/", views.product_feature_edit1, name="product_feature_edit"),
    path("product-features/<int:id>/delete/", views.product_feature_delete1, name="product_feature_delete"),

    path("contacts/", views.contact_list1, name="contact_list"),
    path("contacts/create/", views.contact_create1, name="contact_create"),
    path("contacts/<int:id>/edit/", views.contact_edit1, name="contact_edit"),
    path("contacts/<int:id>/delete/", views.contact_delete1, name="contact_delete"),

    path("internet/", views.internet_list1, name="internet_list"),
    path("internet/create/", views.internet_create1, name="internet_create"),
    path("internet/<int:id>/edit/", views.internet_edit1, name="internet_edit"),
    path("internet/<int:id>/delete/", views.internet_delete1, name="internet_delete"),

    path("missions/", views.mission_list1, name="mission_list"),
    path("missions/create/", views.mission_create1, name="mission_create"),
    path("missions/<int:id>/edit/", views.mission_edit1, name="mission_edit"),
    path("missions/<int:id>/delete/", views.mission_delete1, name="mission_delete"),

    path("mission-points/", views.mission_point_list1, name="mission_point_list"),
    path("mission-points/create/", views.mission_point_create1, name="mission_point_create"),
    path("mission-points/<int:id>/edit/", views.mission_point_edit1, name="mission_point_edit"),
    path("mission-points/<int:id>/delete/", views.mission_point_delete1, name="mission_point_delete"),

    path("statistics/", views.statistic_list1, name="statistic_list"),
    path("statistics/create/", views.statistic_create1, name="statistic_create"),
    path("statistics/<int:id>/edit/", views.statistic_edit1, name="statistic_edit"),
    path("statistics/<int:id>/delete/", views.statistic_delete1, name="statistic_delete"),

    path("values/", views.value_list1, name="value_list"),
    path("values/create/", views.value_create1, name="value_create"),
    path("values/<int:id>/edit/", views.value_edit1, name="value_edit"),
    path("values/<int:id>/delete/", views.value_delete1, name="value_delete"),

    path("achievements/", views.achievement_list1, name="achievement_list"),
    path("achievements/create/", views.achievement_create1, name="achievement_create"),
    path("achievements/<int:id>/edit/", views.achievement_edit1, name="achievement_edit"),
    path("achievements/<int:id>/delete/", views.achievement_delete1, name="achievement_delete"),

    path("members/", views.member_list1, name="member_list"),
    path("members/create/", views.member_create1, name="member_create"),
    path("members/<int:id>/edit/", views.member_edit1, name="member_edit"),
    path("members/<int:id>/delete/", views.member_delete1, name="member_delete"),

    path("histories/", views.history_list1, name="history_list"),
    path("histories/create/", views.history_create1, name="history_create"),
    path("histories/<int:id>/edit/", views.history_edit1, name="history_edit"),
    path("histories/<int:id>/delete/", views.history_delete1, name="history_delete"),
]
