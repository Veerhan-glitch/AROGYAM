from django.urls import path
from arogyam.backend import views
from django.urls import path


urlpatterns = [
    path('home/', views.home, name='home'),
    path('feedback-by-user/', views.feedback_by_user, name='feedback_by_user'),
    path('feedback-by-product/', views.feedback_by_product, name='feedback_by_order'),
    path('orders/', views.user_orders, name='user_orders'),
    path('highest-avg-rated-doctor/', views.highest_avg_rated_doctor_by_specialization, name='highest_avg_rated_doctor'),
    path('doctors-total-visits/', views.doctors_with_total_visits, name='doctors_total_visits'),
    path('user_appointments/', views.user_appointments, name='user_appointments'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('payment-history/', views.user_payments, name='user_payments'),
    path('labtests/', views.lab_tests, name='lab_tests'),
    path('reports/', views.test_reports, name='test_reports'),
    path('submit-ticket/', views.support_ticket, name='submit_ticket'),
    path('support-tickets/', views.user_support_tickets, name='user_support_tickets'),
    path('notifications/', views.user_notifications, name='user_notifications'),
    path('user-offers/', views.user_offers, name='user_offers'),
    path('search-products/', views.search_products, name='search_products'),
    path('product-details/', views.product_details, name='product_details'),
]
