#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^reset_password$', views.ProfileResetPassword.as_view(),
        {'post_reset_redirect': '/customer/post_reset_password',
        'template_name': 'customer/website/customer.reset.password.html',
        'email_template_name': 'customer/website/customer.reset.password.email.html',
        'subject_template_name': 'customer/website/customer.reset.password.subject.txt'},
        name='customer_reset_password'),
    url(r'^post_reset_password$', views.ProfilePostResetPassword.as_view(), name='post_reset_password'),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'customer/website/customer.reset.password.confirm.html',
         'post_reset_redirect': '/customer/password_reset_complete/'},
        name='password_reset_confirm'),
    url(r'^password_reset_complete/', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'customer/website/customer.reset.password.complete.html'},
        name='password_reset_complete'),
    url(r'^signin/$', views.SigninView.as_view(), name='signin'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^to_email_confirm$', views.ToEmailConfirmView.as_view(), name='to_email_confirm'),
    url(r'^email_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.EmailConfirmView.as_view(), name='email_confirm'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout')
)
