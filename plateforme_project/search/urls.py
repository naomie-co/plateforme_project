from django.conf.urls import url

from . import views
"""
urlpatterns = [
    url(r'^$', views.index, name='index/'),
]

"""
#link to namespace in plateforme.urls.py
app_name = 'search'
urlpatterns = [
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name='log_out'),
]

