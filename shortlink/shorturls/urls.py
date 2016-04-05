from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'shorten/', views.create),
    url(r'(?P<pattern>[0-9a-zA-Z]{1,4})$', views.match),
]
