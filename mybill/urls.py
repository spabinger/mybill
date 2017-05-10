from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /mybill/5/

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /mybill/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views., name='vote'),

    url(r'^vote/$', views.vote, name='vote')

]