# -*- coding: utf-8 -*-
import json
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
			obj.publicly = True
			obj.save()
			return HttpResponseRedirect("/")
	else:
		form = PostForm()

	return HttpResponse("error")


def realtime_posts(request):
	'''return posts
	'''
	posts = Post.objects.filter(publicly=True).order_by('last_mod_time')[:1]
	srl = AjaxSerializer()
	data = srl.serialize(posts)
	return HttpResponse(data, mimetype='application/json')



def latest_posts(request):
	'''return posts
	'''
	max = 20
	posts = Post.objects.filter(publicly=True).order_by('last_mod_time')[:max]
	srl = AjaxSerializer()
	data = srl.serialize(posts)
	return HttpResponse(data, mimetype='application/json')
