from django.contrib import admin
from django.urls import path
from .views import (
    home,
    get_feedback_by_order,
    get_feedback_by_user,
    get_appointments,
    get_labtests,
    get_prescriptions,
    get_orders_with_items,
    get_all_doctors,
    get_doctors_by_specialization,
    get_doctors_sorted_by_rating,
    get_doctors_sorted_by_fee,
    get_specializations,
    get_appointments_by_doctor,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/get-feedback-by-order/<int:order_id>/', get_feedback_by_order, name='get_feedback_by_order'),
    path('api/get-feedback-by-user/<int:user_id>/', get_feedback_by_user, name='get_feedback_by_user'),
    path('api/get-appointments/<int:user_id>/', get_appointments, name='get_appointments'),
    path('api/get-labtests/<int:testid>/', get_labtests, name='get_labtests'),
    path('api/get-prescriptions/<int:user_id>/', get_prescriptions, name='get_prescriptions'),
    path('api/get-orders/<int:user_id>/', get_orders_with_items, name='get_orders_with_items'),
    path('api/get-doctors/', get_all_doctors, name='get_all_doctors'),
    path('api/get-doctors/specialization/<str:specialization>/', get_doctors_by_specialization, name='get_doctors_by_specialization'),
    path('api/get-doctors/sort/rating/', get_doctors_sorted_by_rating, name='get_doctors_sorted_by_rating'),
    path('api/get-doctors/sort/fee/', get_doctors_sorted_by_fee, name='get_doctors_sorted_by_fee'),
    path('api/get-specializations/', get_specializations, name='get_specializations'),
    path('api/get-appointments-by-doctor/<int:doctor_id>/', get_appointments_by_doctor, name='get_appointments_by_doctor'),
]
