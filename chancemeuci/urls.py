from django.conf.urls import url
from . import views

app_name = 'chancemeuci'

urlpatterns = [
    # /chancemeuci/
    url(r'^$', views.index.as_view(), name='index'),
]