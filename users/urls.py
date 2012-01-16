from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('microblog.users.views',
    url(r'^register/$', 'register', name='register'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$', 'login', {
			'template_name': 'index.html',
			'redirect_field_name': 'next',}),
	url(r'^logout/$', 'logout', {
			'next_page': '/',}),
)
