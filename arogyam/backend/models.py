# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    phonenumber = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
    
    def __str__(self):
        return str(self.userid)


class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50)
    trackinginfo = models.CharField(max_length=100, blank=True, null=True)
    deliveryoption = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return str(self.orderid)


class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    composition = models.TextField()
    type = models.CharField(max_length=50)
    prescriptionneeded = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return str(self.productid)


class Orderitems(models.Model):
    orderitemid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orderid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderitems'

    def __str__(self):
        return str(self.orderitemid)


class Prescription(models.Model):
    prescriptionid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    filepath = models.TextField()

    class Meta:
        managed = False
        db_table = 'prescription'

    def __str__(self):
        return str(self.prescriptionid)


class Doctor(models.Model):
    doctorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    specialization = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return str(self.doctorid)


class Booksappointment(models.Model):
    appointmentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctorid')
    date = models.DateField()
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'booksappointment'

    def __str__(self):
        return str(self.appointmentid)


class Healthrecords(models.Model):
    recordid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    filepath = models.TextField()

    class Meta:
        managed = False
        db_table = 'healthrecords'

    def __str__(self):
        return str(self.recordid)


class Payments(models.Model):
    paymentid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orderid')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'payments'

    def __str__(self):
        return str(self.paymentid)


class Labtests(models.Model):
    testid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    testdetails = models.TextField()

    class Meta:
        managed = False
        db_table = 'labtests'

    def __str__(self):
        return str(self.testid)


class Reports(models.Model):
    reportid = models.AutoField(primary_key=True)
    filepath = models.TextField()
    testid = models.ForeignKey(Labtests, models.DO_NOTHING, db_column='testid')

    class Meta:
        managed = False
        db_table = 'reports'

    def __str__(self):
        return str(self.reportid)


class Supporttickets(models.Model):
    ticketid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    issuetype = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'supporttickets'

    def __str__(self):
        return str(self.ticketid)


class Feedback(models.Model):
    feedbackid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'feedback'

    def __str__(self):
        return str(self.feedbackid)


class Notifications(models.Model):
    notificationid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')
    message = models.TextField()
    datetime = models.DateTimeField()
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'notifications'

    def __str__(self):
        return str(self.notificationid)


class Offers(models.Model):
    offerid = models.AutoField(primary_key=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    validuntil = models.DateField()

    class Meta:
        managed = False
        db_table = 'offers'

    def __str__(self):
        return str(self.offerid)


class Useroffers(models.Model):
    useroffersid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='userid')
    offerid = models.ForeignKey(Offers, on_delete=models.CASCADE, db_column='offerid')

    class Meta:
        db_table = 'useroffers'
        unique_together = (('userid', 'offerid'),)
        managed = False
        
    def __str__(self):
        return f"User ID: {self.userid}, Offer ID: {self.offerid}"