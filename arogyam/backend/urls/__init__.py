from django.urls import path, include
from arogyam.backend import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('api/', include(('arogyam.backend.urls.customer_urls', 'customer'))),
    path('api/', include(('arogyam.backend.urls.doctor_urls', 'doctor'))),
    path('api/', include(('arogyam.backend.urls.admin_urls', 'admin'))),
]
