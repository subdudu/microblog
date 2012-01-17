# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from posts.models import Post



class PostForm(ModelForm):
	class Meta:
		model = Post
