# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template import loader



def home(request):
	c = RequestContext(request, {
			'title': u'指挥部教导大队博客主页！',
			'user': request.user,
		})
	return HttpResponse(loader.get_template('index.html').render(c))
