from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/', views.single, name='single'),
    url(r'^paired/', views.paired, name='paired'),
    url(r'^$', views.choose, name='choose'),
    url(r'^uploadtest/', views.uploadtest, name='uploadtest'),
    url(r'^loading/', views.loading, name='loading'),
    url(r'^tutorial/', views.tutorial, name='tutorial'),
    url(r'^programmes/', views.programmes, name='programmes'),
    url(r'^about/', views.about, name='about'),
    url(r'^results/', views.results, name='results'),

]