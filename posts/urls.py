from django.contrib import admin
from django.urls import path
from .views import hello, get_index, get_about, get_contacts

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-view"),
    path("contacts/", get_contacts, name="endpoint-contact"),
    path("about/", get_about, name="get-about"),

]