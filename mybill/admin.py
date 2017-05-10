# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Choice, Question, Store


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass



