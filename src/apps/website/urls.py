#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'apps.website.views.index', name='index'),
)

urlpatterns += patterns('',
    url(r'^customer/', include('apps.customer.website.urls', namespace='customer')),
)

urlpatterns += patterns('',
    url(r'^hotel/', include('apps.hotel.website.urls', namespace='hotel')),
)

urlpatterns += patterns('',
    url(r'^flight/', include('apps.flight.website.urls', namespace='flight')),
)

urlpatterns += patterns('',
    url(r'^package/', include('apps.package.website.urls', namespace='package')),
)

urlpatterns += patterns('',
    url(r'^order/', include('apps.order.website.urls', namespace='order')),
)

urlpatterns += patterns('',
    url(r'^present/', include('apps.present.website.urls', namespace='present')),
)

urlpatterns += patterns('',
    url(r'^share/', include('apps.share.website.urls', namespace='share')),
)

urlpatterns += patterns('',
    url(r'^knowledge/', include('apps.knowledge.website.urls', namespace='knowledge')),
)