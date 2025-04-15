from django.urls import path
from arogyam.backend import views

urlpatterns = [
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor-schedule/', views.doctor_schedule, name='doctor_schedule'),
    path('doctor-feedback/', views.doctor_feedback, name='doctor_feedback'),
    path('health-records/', views.health_records, name='health_records'),
    path('doctor-profile/', views.doctor_profile, name='doctor_profile'),
    path('update-doctor-rating/', views.update_doctor_rating, name='update_doctor_rating'),
    path('appointments-by-doctor/', views.get_appointments_by_doctor, name='appointments_by_doctor'),
    path('doctors/', views.all_doctors, name='all_doctors'),
    path('doctors/filter/', views.filter_doctors_by_specialization, name='filter_doctors_by_specialization'),
    path('doctors/sort/rating/', views.sort_doctors_by_rating, name='sort_doctors_by_rating'),
    path('doctors/sort/fee/', views.sort_doctors_by_fee, name='sort_doctors_by_fee'),
    path('doctor-specializations/', views.get_specialization_values, name='doctor_specializations'),
]
