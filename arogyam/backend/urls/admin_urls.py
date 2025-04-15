from django.urls import path
from arogyam.backend import views

urlpatterns = [
    path('all-users/', views.all_users, name='all_users'),
    path('add-user/', views.add_user, name='add_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-product/', views.add_product, name='add_product'),
    path('update-product-price/', views.update_product_price, name='update_product_price'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('most-ordered-products/', views.get_most_ordered_products, name='most_ordered_products'),
    path('add-lab-test/', views.add_lab_test, name='add_lab_test'),
    path('link-report/', views.link_report, name='link_report'),
    path('all-offers/', views.all_offers, name='all_offers'),
    path('send-notification/', views.send_notification, name='send_notification'),
    path('high-value-customers/', views.high_value_customers, name='high_value_customers'),
    path('users-with-orders-feedback/', views.users_with_orders_and_feedback, name='users-with-orders-feedback/'),
    path('doctors-ratings/', views.list_doctors_ratings, name='list_doctors_ratings'),
    path('top-revenue-products-prescription-users/', views.top_revenue_products_for_prescription_users, name='top_revenue_products_prescription_users'),
    path('recent-doctor-appointments/', views.recent_doctor_appointments_with_avg_fee, name='recent_doctor_appointments'),
    path('users-spending-with-offers/', views.user_order_spending_with_offers, name='users_spending_with_offers'),
    path('recent-active-users/', views.users_with_recent_activity, name='recent_active_users'),
    path('users-prescription-orders/', views.users_who_ordered_prescription_products, name='users_prescription_orders'),
    path('patient-medical-summary/', views.patient_medical_summary, name='patient_medical_summary'),
    path('user-order-history/', views.user_order_history, name='user_order_history')
]
