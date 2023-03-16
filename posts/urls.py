from django.contrib import admin
from django.urls import path
from .views import hello, get_index, get_about, get_contacts, get_post, update_post, delete_post

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path("contacts/", get_contacts, name="contacts-page"),
    path("about/", get_about, name="about-page"),
    path("getpost/", get_post, name = "get-post"),
    path("update/", update_post, name="update-post"),
    path('delete/', delete_post, name="delete-post"),
]