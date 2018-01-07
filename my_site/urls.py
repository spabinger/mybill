"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from mybill import views as mybill_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', mybill_views.home, name='home'),

    url(r'^about/$', mybill_views.about, name='about'),

    url(r'^add_store/$', mybill_views.StoreAddView.as_view(), name='add_store'),
    url(r'^view_store/(?P<pk>[-\w]+)', mybill_views.StoreDetailView.as_view(), name='view_store'),
    url(r'^stores/$', mybill_views.StoreListView.as_view(), name='stores'),

    url(r'^add_store_brand/$', mybill_views.StoreBrandAddView.as_view(), name='add_store_brand'),
    url(r'^store_brands/$', mybill_views.StoreBrandListView.as_view(), name='store_brands'),

    url(r'^add_store_type/$', mybill_views.StoreTypeAddView.as_view(), name='add_store_type'),
    url(r'^store_types/$', mybill_views.StoreTypeListView.as_view(), name='store_types'),

    url(r'^bills/$', mybill_views.BillListView.as_view(), name='bills'),
    url(r'^view_bill/(?P<pk>[-\w]+)', mybill_views.BillDetailView.as_view(), name='view_bill'),
    url(r'^add_bill_simple$', mybill_views.add_bill_simple, name='add_bill_simple'),
    url(r'^add_bill_complex$', mybill_views.add_bill_complex, name='add_bill_complex'),

    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),

]
