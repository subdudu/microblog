# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	"""帖子，可以设置为public（公开的）或者 limited（有限共享）
	"""
	content = models.TextField(verbose_name=_(u"内容"),
			max_length=9000,
		)
	created_by = models.ForeignKey(User,
			verbose_name=_(u"发布者"),
			editable = False,
		)
	last_mod_time = models.DateTimeField(verbose_name=_(u"最后更改时间"),
			auto_now=True,
		)
	publicly = models.BooleanField(verbose_name=_(u"是否公开给所有人"),
			default=False,
		)

	def __unicode__(self):
		return unicode(self.id)
