from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^user/(\w+)/$', views.user_page),
	url(r'^profile/(.*)/$', views.dataCollected, name='profile'),
	url(r'^forms/$', views.get_name, name='forms'),
	url(r'^signup/$', views.signup, name='signup'),
]