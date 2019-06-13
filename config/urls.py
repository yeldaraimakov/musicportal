from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include('portal.admin_side.urls')),

    path('', include('portal.music_portal.urls')),

    path('api/', include('portal.music_portal.api.urls'))
]
