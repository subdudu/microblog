# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Circle(models.Model):
	"""圈子
	"""
	name = models.TextField(verbose_name=_(u"名称"),
			max_length=64,
		)
	created_by = models.ForeignKey(User,
			verbose_name=_(u"创建者"),
			editable = False,
		)

	def __unicode__(self):
		return self.name



class CircleUser(models.Model):
	'''Circle has users
	'''
	circle = models.ForeignKey(Circle,
		verbose_name=_(u"圈子"),
		)
	user = models.ForeignKey(User,
		verbose_name=_(u"朋友"),
		)

	def __unicode__(self):
		return "%s-%s" % (self.circle, self.user)
