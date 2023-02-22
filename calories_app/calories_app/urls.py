from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ResumeX",
      default_version='v1',
      description="AI-Powered Smart Recruitment Portal",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gtlrajpatel@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('calories_tracker.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    ]

admin.site.site_header = 'Calories App Administration'
admin.site.index_title = 'Calories App Admin'
admin.site.site_title = 'Calories App Administration'
