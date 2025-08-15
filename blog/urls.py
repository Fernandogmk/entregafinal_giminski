# blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("pages/", views.PageListView.as_view(), name="page_list"),
    path("pages/create/", views.PageCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/edit/", views.PageUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
]
