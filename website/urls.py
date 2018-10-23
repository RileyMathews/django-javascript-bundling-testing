from website import views
from django.conf.urls import url
from django.urls import path

app_name = "website"
urlpatterns=[
    path('', views.index, name="index")
]