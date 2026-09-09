from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crm import views as crm_views


urlpatterns = [

    path('admin/', admin.site.urls),

    # CRM
    path('', include('crm.urls')),

    # Custom Users / Login
    path('', include('users.urls')),

    # Custom Password Change
    path(
        'password_change/',
        crm_views.CustomPasswordChangeView.as_view(),
        name='password_change'
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )