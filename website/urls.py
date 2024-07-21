from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('manage/', include('manage.urls')),
    # path('accounts/', include('allauth.urls')),
]
