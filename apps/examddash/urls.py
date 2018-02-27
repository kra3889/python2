from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^logout$',views.logout),
    url(r'^home$', views.success),
    url(r'^examdpoke/(?P<id>\d+)$', views.examdpoke, name='examdpoke'),

]
