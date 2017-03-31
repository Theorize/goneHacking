from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^$', views.index),
url(r'^profile/$', views.profile),
url(r'^userhome/$', views.user_home),
url(r'^profile/post_url/$', views.post_status),
url(r'^cantask_manager', views.cantask_network),
url(r'^cantask_close_rels', views.cantask_close_relatives),
url(r'^cantask_rels', views.cantask_relatives)
]
