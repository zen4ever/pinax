from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^username_autocomplete/$', 'autocomplete_app.views.username_autocomplete_friends', name='profile_username_autocomplete'),
    url(r'^$', 'profiles.views.profiles', name='profile_list'),
    url(r'^profile/(?P<username>[\w\._-]+)/$', 'profiles.views.profile', name='profile_detail'),
    url(r'^edit/$', 'profiles.views.profile_edit', name='profile_edit'),
    url(r'^invite/(?P<username>[\w\._-]+)/$', 'profiles.views.invite_as_friend', name="profile_invite_as_friend"),
)
