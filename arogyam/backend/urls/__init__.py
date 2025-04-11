from django.urls import path, include
from arogyam.backend import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('user/', views.user, name='home'),
    path('api/', include(('arogyam.backend.urls.customer_urls', 'customer'))),
    path('api/', include(('arogyam.backend.urls.doctor_urls', 'doctor'))),
    path('api/', include(('arogyam.backend.urls.admin_urls', 'admin'))),
]
