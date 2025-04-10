from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # The Django admin panel:
    path('admin/', admin.site.urls),
    # Delegate all other URLs to the backend app.
    path('', include('arogyam.backend.urls')),
]
