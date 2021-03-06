#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^$', 'apps.admin.views.home', name='admin_home'),
    url(r'^dashboard$', 'apps.admin.views.dashboard', name='dashboard'),
    url(r'^foundation/', include('apps.foundation.urls', namespace='foundation')),
    url(r'^account/', include('apps.account.urls', namespace='account')),
    url(r'^customer/', include('apps.customer.admin.urls', namespace='customer')),
    url(r'^tour/', include('apps.tour.admin.urls', namespace='tour')),
    url(r'^hotel/', include('apps.hotel.admin.urls', namespace='hotel')),
    url(r'^flight/', include('apps.flight.admin.urls', namespace='flight')),
    url(r'^package/', include('apps.package.admin.urls', namespace='package')),
    url(r'^present/', include('apps.present.admin.urls', namespace='present')),
    url(r'^order/', include('apps.order.admin.urls', namespace='order')),
    url(r'^thirdparty/', include('apps.thirdparty.urls', namespace='thirdparty')),
    url(r'^initdata/$', 'apps.admin.views.initdata'),
    url(r'^share/', include('apps.share.admin.urls', namespace='share')),
    url(r'^knowledge/', include('apps.knowledge.admin.urls', namespace='knowledge')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^loaddata/(?P<filename>.*)', 'apps.admin.views.loaddata'),
    )
