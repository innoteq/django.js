# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from os.path import join, isdir

from django.conf.urls import url
from django.views.i18n import javascript_catalog
from django.apps import apps

from djangojs.conf import settings
from djangojs.views import UrlsJsonView, ContextJsonView, JsInitView


def js_info_dict():
    js_info_dict = {
        'packages': [],
    }

    for app in apps.get_app_configs():
        if settings.JS_I18N_APPS and app.label not in settings.JS_I18N_APPS:
            continue
        if settings.JS_I18N_APPS_EXCLUDE and app.label in settings.JS_I18N_APPS_EXCLUDE:
            continue
        for path in app.path:
            if isdir(join(path, 'locale')):
                js_info_dict['packages'].append(app.name)
                break
    return js_info_dict


urlpatterns = [
    url(r'^init\.js$', JsInitView.as_view(), name='django_js_init'),
    url(r'^urls$', UrlsJsonView.as_view(), name='django_js_urls'),
    url(r'^context$', ContextJsonView.as_view(), name='django_js_context'),
    url(r'^translation$', javascript_catalog, js_info_dict(), name='js_catalog'),
]
