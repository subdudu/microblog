from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('microblog.posts.views',
    url(r'^add/$', 'add', name='add_post'),
    url(r'^realtime_posts/$', 'realtime_posts', name='realtime_posts'),
    url(r'^latest_posts/$', 'latest_posts', name='latest_posts'),
)
