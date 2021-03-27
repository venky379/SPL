from . import views
from django.conf.urls import url
urlpatterns = [
 url(r'^$', views.home, name = "home"),
 url(r'^team_register', views.team_register),
 url(r'^feesummary', views.feesummary),
 url(r'^schedule', views.schedule, name='schedule'),
 url(r'^player_list', views.player_list),
 url(r'^user_register/(?P<team_id>[\w.@+-]+)/$', views.user_register),
 url(r'^user_edit/(?P<team_id>[\w.@+-]+)/(?P<user_id>[\w.@+-]+)/$', views.user_edit),
 url(r'^team_edit/(?P<team_id>[\w.@+-]+)$', views.team_edit),

]