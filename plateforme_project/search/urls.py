from django.conf.urls import url, include

from . import views
"""
urlpatterns = [
    url(r'^$', views.index, name='index/'),
]

"""
#link to namespace in plateforme.urls.py
app_name = 'search'
urlpatterns = [
    #url(r'^listing/$', views.listing, name='listing'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^products/$', views.products, name='products'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^my_selection/$', views.my_selection, name='my_selection'),

]

