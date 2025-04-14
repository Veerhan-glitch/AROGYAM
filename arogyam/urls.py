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
    # path('logout/', views.logout_view, name='logout'),
    path('', include('arogyam.backend.urls')),
]
