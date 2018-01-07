# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import resolve
#from .views import home


from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    #def test_home_url_resolves_home_view(self):
    #    view = resolve('/')
    #    self.assertEquals(view.func, home)