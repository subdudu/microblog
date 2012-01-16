# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def register(request):
	if request.user.is_authenticated():
		return render_to_response('register.html', {
				'has_account': True,
			})
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				form.cleaned_data['username'],
				'',
				form.cleaned_data['password1'],
				)
			user.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()

	c = RequestContext(request, {
			'title': u'武警黄金技术学校欢迎您！',
			'form': form,
		})
	return HttpResponse(loader.get_template('users/register.html').render(c))
