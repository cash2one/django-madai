#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from django.template.response import TemplateResponse
from apps.tour.models import Article, Scenery, GuideType

logger = logging.getLogger('apps.' + os.path.basename(os.path.dirname(__file__)))


def index(request):
    return TemplateResponse(request, 'website/index.html', locals())


def legal(request):
    return TemplateResponse(request, 'website/legal.inc.html')


def privacy(request):
    return TemplateResponse(request, 'website/privacy.inc.html')


def aboutus(request):
    return TemplateResponse(request, 'website/aboutus.html')


def package_searching(request):
    return TemplateResponse(request, 'website/package.searching.html')