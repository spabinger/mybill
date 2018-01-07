# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


### Groceries, Electric, ...
class StoreType(models.Model):
    store_type = models.CharField(max_length=300)

    def get_fields_generic_view(self):
        return [field.value_to_string(self) for field in StoreType._meta.fields]

    def get_field_names_generic_view(self):
        return StoreType._meta.fields

    def __str__(self):
        return self.store_type


### Something like 'Billa'
class StoreBrand(models.Model):
    name = models.CharField(max_length=300)
    store_type = models.ForeignKey(StoreType)

    def get_fields_generic_view(self):
        return [field.value_to_string(self) for field in StoreBrand._meta.fields]

    def get_field_names_generic_view(self):
        return StoreBrand._meta.fields

    def __str__(self):
        return "%s (%s)" % (self.name, self.store_type)



class Store(models.Model):
    name = models.CharField(max_length=300)
    brand = models.ForeignKey(StoreBrand)   # e.g.: Billa


    def get_fields_generic_view(self):
        return [field.value_to_string(self) for field in Store._meta.fields]

    def get_field_names_generic_view(self):
        return Store._meta.fields

    def __str__(self):
        return "%s (%s)" % (self.name, self.brand)


class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    direction = None
    created_by = models.ForeignKey(User, related_name='transactions')


class Bill(Transaction):
    store = models.ForeignKey(Store)
    image = models.ImageField(upload_to='images/')
    direction = "outgoing"

    def __str__(self):
        return "%s: %f" % (self.store, self.amount)








## Information

## If no migrations folder has been built run
## -) python3 manage.py makemigrations audena



## Always make migrations when changing
## 1) python3 manage.py makemigrations
## 2) python3 manage.py sqlmigrate audena 0001       ## check the SQL statements
## 3) python3 manage.py migrate


## Drop all tables
## python3 manage.py dbshell
## select 'drop table ' || name || ';' from sqlite_master where type = 'table';
