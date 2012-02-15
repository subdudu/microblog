# -*- coding: utf-8 -*-
import json
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template import loader
from models import Post
from forms import PostForm



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



def ajax_posts_data(posts):
	result = []
	for p in posts:
		result.append({
			"user_name": p.created_by.username,
			"user_image": "/static/images/portrait.jpg",
			"content": p.content,
			"last_mod_time": p.last_mod_time.strftime('%Y-%m-%d %H:%M:%S'),
			"publicly": p.publicly,
			})
	return result



def realtime_posts(request):
	'''return posts
	'''
	access_time = datetime.utcnow().strptime(request.session['access_time'], '%Y-%m-%dT%H:%M:%S.%f')
	posts = Post.objects.filter(publicly=True).filter(last_mod_time__gt=access_time).order_by('last_mod_time')[:1]
	data = json.dumps(ajax_posts_data(posts))
	request.session['access_time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
	return HttpResponse(data, mimetype='application/json')



def latest_posts(request):
	'''return posts
	'''
	max = 20
	posts = Post.objects.filter(publicly=True).order_by('-last_mod_time')[:max]
	data = json.dumps(ajax_posts_data(posts))
	request.session['access_time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
	return HttpResponse(data, mimetype='application/json')
