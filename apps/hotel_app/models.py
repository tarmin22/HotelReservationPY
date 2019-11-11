from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    credit_card_number = models.BigIntegerField()
    expiration_month = models.IntegerField()
    expiration_year = models.IntegerField()
    cvv =  models.PositiveIntegerField() 
    credit_card_type = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    zip_code = models.PositiveIntegerField() 
    state = models.CharField(max_length=45)
    paid_by = models.ForeignKey(User, related_name="payments") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Room(models.Model):
    name = models.CharField(max_length=45)
    rate = models.DecimalField(max_digits=6,decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Reservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    created_by = models.ForeignKey(User, related_name="reservations")
    payment_info = models.ForeignKey(Payment, related_name="reservations")
    room_type = models.ForeignKey(Room, related_name="reservations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




