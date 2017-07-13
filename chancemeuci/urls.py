from django.conf.urls import url
from . import views

app_name = 'chancemeuci'

urlpatterns = [
    # /chancemeuci/
    url(r'^$', views.index.as_view(), name = 'index'),
    # /chancemeuci/datasource
    url(r'^datasource/$', views.datasource, name = 'datasource'),
    # /chancemeuci/development
    url(r'^development/$', views.development, name='development'),
    # /chancemeuci/comments
    url(r'^comments/$', views.comments, name='comments'),
    # /chancemeuci/notes
    url(r'^notes/$', views.notes, name = 'notes'),
]