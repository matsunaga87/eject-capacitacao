from django.conf.urls import url, include, patterns

urlpatterns = patterns('simplemooc.core.views',
    url(r'^contato/$', 'contact',name='contact'),	
    url(r'^$', 'home',name='home'),	
)