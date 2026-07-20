from django.urls import path
from . import views

app_name = "post"

urlpatterns = [

    path("post/", views.index, name="index"),

    path("post/create/", views.create, name="create"),

]