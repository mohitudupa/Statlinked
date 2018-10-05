from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^register/', views.register, name='register'),
    url(r'^hub/', views.hub, name='hub'),
    url(r'^logout/', views.user_logout, name='user_logout'),
]