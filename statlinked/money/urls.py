from django.conf.urls import url
from . import views


app_name = 'money'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^history/', views.history, name='history'),
    url(r'^add_bill/', views.add_bill, name='add_bill'),
    url(r'^edit_bill/', views.edit_bill, name='edit_bill'),
    url(r'^del_bill/', views.del_bill, name='del_bill'),
    url(r'^update_goal/', views.update_goal, name='update_goal'),
]
