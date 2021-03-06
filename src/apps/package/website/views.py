#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
import sys
from apps.package.models import Package
from django.shortcuts import render_to_response
from django.template import RequestContext


def searching(request):
    start_address = request.GET['start_address']
    start_date = request.GET['start_date']
    price_range = request.GET['price_range']

    # # TEST CODE # #
    # package = Package.active_objects.all()[0]
    # start_address = u'成都'
    # import datetime
    # start_date = datetime.date(2014, 5, 1)
    # price_min = 1000
    # price_max = 3000
    # # END TEST # #
    packages = Package.active_objects.filter(is_published=True).select_related('hotels', 'flights').filter(
        start_city=start_address,
        price=price_range,
        start_date__lte=start_date,
        end_date__gte=start_date)

    if packages.count():
        # FIXME 多个package如何挑选, 暂时选第一个
        package = packages[0]
        return render_to_response('package/website/package.searching.html',
                                  locals(),
                                  context_instance=RequestContext(request))
    else:
        #TODO 无套餐需要个空套餐页面
        return render_to_response('package/website/package.noresult.html',
                                  locals(),
                                  context_instance=RequestContext(request))