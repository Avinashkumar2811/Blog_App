from django.urls import path
from . import views
from .views import bloglists,blogdetails, createpost, updatepost, deletepost

urlpatterns = [
    path("",bloglists.as_view(),name="bloglist"),
    path("<int:pk>/",blogdetails.as_view(),name="blogdetail"),
    path("create/",createpost.as_view(),name="createpost"),
    path("create/<int:pk>/",updatepost.as_view(),name="updatepost"),
    path("delete/<int:pk>/",deletepost.as_view(),name="deletepost")
]


#name= ka use hum direct url pe jane ke liye karte hain