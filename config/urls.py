from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('language_selector.urls')),
    path('uz/', include(('medical.urls', 'medical'), namespace='uz')),
    path('ru/', include(('medical_ru.urls', 'medical_ru'), namespace='ru')),
    path('en/', include(('medical_en.urls', 'medical_en'), namespace='en')),
    path('uz/admin/', include(('dashboard.urls', 'dashboard'), namespace='uz-admin')),
    path('ru/admin/', include(('dashboard_ru.urls', 'dashboard_ru'), namespace='ru-admin')),
    path('en/admin/', include(('dashboard_en.urls', 'dashboard_en'), namespace='en-admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
