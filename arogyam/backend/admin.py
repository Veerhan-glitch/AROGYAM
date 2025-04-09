from django.contrib import admin
from .models import (
    Users, 
    Orders, 
    Product, 
    Orderitems, 
    Prescription, 
    Doctor, 
    Booksappointment, 
    Healthrecords, 
    Payments, 
    Labtests, 
    Reports, 
    Supporttickets, 
    Feedback, 
    Notifications, 
    Offers, 
    Useroffers
)

admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Orderitems)
admin.site.register(Prescription)
admin.site.register(Doctor)
admin.site.register(Booksappointment)
admin.site.register(Healthrecords)
admin.site.register(Payments)
admin.site.register(Labtests)
admin.site.register(Reports)
admin.site.register(Supporttickets)
admin.site.register(Feedback)
admin.site.register(Notifications)
admin.site.register(Offers)
admin.site.register(Useroffers)
