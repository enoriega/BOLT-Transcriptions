from django.conf.urls import patterns, url
from django.views.generic import TemplateView

import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^arabic/?$', views.arabic, name='arabic'),
    #url(r'^english/?$', views.english, name='english'),
    url(r'^done/?$', TemplateView.as_view(template_name="transcriptions/done.html"), name='done'),
    url(r'^$', TemplateView.as_view(template_name="transcriptions/done.html"), name='done_2'),
)
