# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template import loader
from django.core import serializers
from posts.models import Post
from posts.forms import PostForm



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
	max = 20
	posts = Post.objects.filter(publicly=True).order_by('last_mod_time')[:max]
	data = serializers.serialize("json", posts, ensure_ascii=False)
	return HttpResponse(data)
