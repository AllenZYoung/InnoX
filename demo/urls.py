from django.conf.urls import url

from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^commentsnum/', views.CommentsCount, name='commentscount'),
    url(r'^freq/',views.Frequency,name='freq'),
]
