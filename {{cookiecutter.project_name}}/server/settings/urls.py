"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)
from health_check import urls as health_urls

from server.apps.common import urls as common_urls
from server.apps.common.views import index


def trigger_error(request):
    division_by_zero = 1 / 0


admin.autodiscover()

urlpatterns = [
    # Apps:
    path('common/', include(common_urls, namespace='common')),

    # Health checks:
    path('health/', include(health_urls)),

    # django-admin:
    path('admin/doc/', include(admindocs_urls)),
    path('admin/', admin.site.urls),

    # Sentry debug trigger error
    path('sentry-debug/', trigger_error),

    # It is a good practice to have explicit index view:
    path('', index, name='index'),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),
        *urlpatterns,
        # Serving media files in development only:
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/',
             SpectacularSwaggerView.as_view(url_name='schema'),
             name='swagger-ui'),
        path('api/schema/redoc/',
             SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
