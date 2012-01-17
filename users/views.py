# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()

	c = RequestContext(request, {
			'title': u'新用户注册！',
			'form': form,
		})
	return HttpResponse(loader.get_template('users/register.html').render(c))
