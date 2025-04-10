from django.urls import path
from arogyam.backend import views

urlpatterns = [
    path('feedback-by-user/', views.feedback_by_user, name='feedback_by_user'),
    path('feedback-by-order/', views.feedback_by_order, name='feedback_by_order'),
    path('orders/', views.user_orders, name='user_orders'),
    path('appointments/', views.user_appointments, name='user_appointments'),
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
