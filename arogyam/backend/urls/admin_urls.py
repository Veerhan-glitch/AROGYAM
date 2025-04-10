from django.urls import path
from arogyam.backend import views

urlpatterns = [
    path('all-users/', views.all_users, name='all_users'),
    path('add-user/', views.add_user, name='add_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-product/', views.add_product, name='add_product'),
    path('update-product-price/', views.update_product_price, name='update_product_price'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('sales-by-month/', views.get_sales_by_month, name='sales_by_month'),
    path('most-ordered-products/', views.get_most_ordered_products, name='most_ordered_products'),
    path('add-lab-test/', views.add_lab_test, name='add_lab_test'),
    path('link-report/', views.link_report, name='link_report'),
    path('all-offers/', views.all_offers, name='all_offers'),
    path('send-notification/', views.send_notification, name='send_notification'),
]
