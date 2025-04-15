from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from arogyam.backend import views

urlpatterns = [
    # The Django admin panel:
    path('admin/', admin.site.urls),
    # Delegate all other URLs to the backend app.
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='Register'),
    path('apitest/', views.index, name='index'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('api/appointments/', views.get_appointments, name='appointments'),
    path('logout/', views.logout, name='logout'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    # path('logout/', views.logout_view, name='logout'),
    path('', include('arogyam.backend.urls')),
]
