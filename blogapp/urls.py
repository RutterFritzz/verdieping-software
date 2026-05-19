from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.create_blog, name="create_blog"),
    path("edit/<int:pk>/", views.edit_blog, name="edit_blog"),
    path("delete/<int:pk>/", views.delete_blog, name="delete_blog"),
]