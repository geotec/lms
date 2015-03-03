from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    # ex: /courses/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /courses/5/
    url(r'^(?P<pk>\d+)$', views.DetailsView.as_view(), name='details'),
    # ex: /course/add
    url(r'^add$', views.AddView.as_view(), name='add'),
    # ex: /courses/5/change/
    url(r'^(?P<pk>\d+)/change$', views.ChangeView.as_view(), name='change'),

    url(r'^save$',views.save, name='save'),
    url(r'^save/(?P<course_id>\w+)/$',views.save, name='save'),
)






