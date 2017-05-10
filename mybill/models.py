# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
   question = models.ForeignKey(Question)
   choice_test = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)

   def __str__(self):
       return self.choice_test


###
### mybill things
###

class Person():
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)



### Groceries, Electric, ...
class StoreType(models.Model):
    type = models.CharField(max_length=300)


### Billa
class StoreBrand(models.Model):
    name = models.CharField(max_length=300)
    type = models.ForeignKey(StoreType)



class Store(models.Model):
    name = models.CharField(max_length=300)
    brand = models.ForeignKey(StoreBrand)   # e.g.: Billa



class Bill(models.Model):
    store = models.ForeignKey(Store)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return "%s: %f" % (self.store, self.amount)


