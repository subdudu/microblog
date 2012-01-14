# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.template.context import RequestContext
from django.template import loader



def home(request):
	c = RequestContext(request, {
			'title': u'武警黄金技术学校欢迎您！',
		})
	return HttpResponse(loader.get_template('index.html').render(c))
