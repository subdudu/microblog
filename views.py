# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.template.context import RequestContext
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm



def home(request):
	if request.user.is_authenticated():
		c = RequestContext(request, {
				'title': u'武警黄金技术学校欢迎您！',
			})
	else:
		form = AuthenticationForm()
		c = RequestContext(request, {
				'title': u'武警黄金技术学校欢迎您！',
				'form': form,
				'next': '/',
			})
	return HttpResponse(loader.get_template('index.html').render(c))
