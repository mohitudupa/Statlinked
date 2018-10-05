from django.conf.urls import url
from . import views


app_name = 'health'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
