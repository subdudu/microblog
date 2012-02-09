# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template import loader
from models import Post
from forms import PostForm
from core.serializer.json import AjaxSerializer



def add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.created_by = request.user
			obj.last_mod_time = datetime.utcnow()
			obj.publicly = True
			obj.save()
			return HttpResponseRedirect("/")
	else:
		form = PostForm()

	return HttpResponse("error")


def realtime_posts(request):
	'''return posts
	'''
	access_time = datetime.utcnow().strptime(request.session['access_time'], '%Y-%m-%dT%H:%M:%S')
	posts = Post.objects.filter(publicly=True).filter(last_mod_time__gt=access_time).order_by('last_mod_time')[:1]
	srl = AjaxSerializer()
	data = srl.serialize(posts)
	request.session['access_time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
	return HttpResponse(data, mimetype='application/json')



def latest_posts(request):
	'''return posts
	'''
	max = 20
	posts = Post.objects.filter(publicly=True).order_by('-last_mod_time')[:max]
	srl = AjaxSerializer()
	data = srl.serialize(posts)
	request.session['access_time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
	return HttpResponse(data, mimetype='application/json')
