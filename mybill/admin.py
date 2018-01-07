# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Store



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass



