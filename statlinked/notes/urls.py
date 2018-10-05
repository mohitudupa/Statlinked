from django.conf.urls import url
from . import views


app_name = 'notes'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_note/', views.add_note, name='add_note'),
    url(r'^edit_note/', views.edit_note, name='edit_note'),
    url(r'^del_note/', views.del_note, name='del_note'),
]