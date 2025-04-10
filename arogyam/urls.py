from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # Admin and Home
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    # ---------- CUSTOMER ENDPOINTS ----------
    # (All expect POST requests, so CSRF protection is disabled for demo)
    path('api/feedback-by-user/', views.feedback_by_user, name='feedback_by_user'),
    path('api/feedback-by-order/', views.feedback_by_order, name='feedback_by_order'),
    path('api/orders/', views.user_orders, name='user_orders'),
    path('api/appointments/', views.user_appointments, name='user_appointments'),
    path('api/prescriptions/', views.prescriptions, name='prescriptions'),
    path('api/book-appointment/', views.book_appointment, name='book_appointment'),
    path('api/payment-history/', views.user_payments, name='user_payments'),
    path('api/labtests/', views.lab_tests, name='lab_tests'),
    path('api/reports/', views.test_reports, name='test_reports'),
    path('api/submit-ticket/', views.support_ticket, name='support_ticket'),
    path('api/support-tickets/', views.user_support_tickets, name='user_support_tickets'),
    path('api/notifications/', views.user_notifications, name='user_notifications'),
    path('api/user-offers/', views.user_offers, name='user_offers'),
    path('api/search-products/', views.search_products, name='search_products'),
    path('api/product-details/', views.product_details, name='product_details'),

    # ---------- DOCTOR ENDPOINTS ----------
    path('api/doctor-schedule/', views.doctor_schedule, name='doctor_schedule'),
    path('api/doctor-feedback/', views.doctor_feedback, name='doctor_feedback'),
    path('api/health-records/', views.health_records, name='health_records'),
    path('api/doctor-profile/', views.doctor_profile, name='doctor_profile'),
    path('api/update-doctor-rating/', views.update_doctor_rating, name='update_doctor_rating'),
    path('api/appointments-by-doctor/', views.get_appointments_by_doctor, name='appointments_by_doctor'),
    # For filtering and sorting doctors (each as separate endpoints)
    path('api/doctors/', views.all_doctors, name='all_doctors'),
    path('api/doctors/filter/', views.filter_doctors_by_specialization, name='filter_doctors_by_specialization'),
    path('api/doctors/sort/rating/', views.sort_doctors_by_rating, name='sort_doctors_by_rating'),
    path('api/doctors/sort/fee/', views.sort_doctors_by_fee, name='sort_doctors_by_fee'),
    path('api/doctor-specializations/', views.get_specialization_values, name='doctor_specializations'),

    # ---------- ADMIN ENDPOINTS ----------
    path('api/all-users/', views.all_users, name='all_users'),
    path('api/add-user/', views.add_user, name='add_user'),
    path('api/delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('api/add-product/', views.add_product, name='add_product'),
    path('api/update-product-price/', views.update_product_price, name='update_product_price'),
    path('api/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/sales-by-month/', views.get_sales_by_month, name='sales_by_month'),
    path('api/most-ordered-products/', views.get_most_ordered_products, name='most_ordered_products'),
    path('api/add-lab-test/', views.add_lab_test, name='add_lab_test'),
    path('api/link-report/', views.link_report, name='link_report'),
    path('api/all-offers/', views.all_offers, name='all_offers'),
    path('api/send-notification/', views.send_notification, name='send_notification'),
]
