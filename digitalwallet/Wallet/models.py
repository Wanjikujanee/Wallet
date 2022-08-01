
from dataclasses import fields
from datetime import datetime
from email.headerregistry import Address
from email.policy import default
from locale import currency
from threading import activeCount
from tkinter import ON
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, FileField, IntegerField
from psycopg2 import Date

class Customer(models.Model):
    first_name=models.CharField( max_length=15)
    last_name=models.CharField( max_length=15)
    gender=models.CharField( max_length=1)
    Address=models.TextField()
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=15)
    id=models.IntegerField()
    phone_number=models.CharField(max_length=15)
    email=models.CharField(max_length=15)
    profile_picture=models.ImageField() 
    # marital_status=models.IntegerField()
    signature=models.ImageField()
    employment=models.BooleanField()
    
class Wallet(models.Model):
    balance=models.IntegerField()
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,null=True)
    pin=models.SmallIntegerField()
    # currency=models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Reward')
    active=models.BooleanField()
    type=models.CharField( max_length=50)
    date_created=models.DateTimeField(default=datetime.now)
 
class Account(models.Model):
    # attribute=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Account') 
    account_type=models.CharField(max_length=23,null=True)
    account_Name=models.CharField(max_length=15)
    savings=models.BooleanField()
    Wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Account')
    # Destination=models.ForeignKey()
    
         
class ThirdParty(models.Model):
    fullname=models.CharField(max_length=15) 
    email=models.EmailField() 
    phone_number=models.CharField(max_length=15) 
    transaction_cost=models.IntegerField()
    # currency=models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Thirdparty')
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Thirdparty_b')
    active=models.BooleanField()
    
class Transaction(models.Model):
    transaction_type=models.CharField(max_length=15)  
    account_origin=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction')
    destination=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_b')
    thirdparty=models.ForeignKey(to=ThirdParty,on_delete=models.CASCADE,related_name='Transaction_third')
    date_and_time=models.DateTimeField(default=datetime)
    receipt=models.CharField(max_length=12)
    status=models.CharField(max_length=10)
     
class Card(models.Model):
    date_of_issue=models.DateTimeField(default=datetime.now)
    card_status=models.CharField(max_length=13)
    Security_Code=models.PositiveSmallIntegerField()
    signature=models.ImageField()
    issuer=models.CharField(max_length=13)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Reward')

     
class Notifications(models.Model):
    date_created=models.DateTimeField(default=datetime.now)
    Message=models.TextField()
    recipient=models.ForeignKey('recipient',on_delete=models.CASCADE,related_name='Notifications')
    isactive=models.BooleanField()
    image=models.ImageField ()  

class Reciept(models.Model):
    date=models.DateTimeField(default=datetime.now,auto_now=False)
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Receipt')
    receipt_file=models.FileField()


class Loan (models.Model):
    Loan_type=models.CharField(max_length=15)
    amount=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Loan')
    Date_and_time=models.DateTimeField(default=datetime.now,auto_now=False)
    Loanterms=models.CharField(max_length=13)
    payment_due_date=models.DateTimeField(default=datetime.now,auto_now=False)
    guaranter=models.CharField(max_length=13)
    balance=models.IntegerField()
    duration=models.CharField(max_length=10)
    interest_rate=models.IntegerField()
    balance=models.IntegerField()
    status=models.CharField(max_length=12)
     
class Reward(models.Model):  
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Reward')
    points=models.PositiveIntegerField()
    date=models.DateTimeField()
    transaction=models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reward')

