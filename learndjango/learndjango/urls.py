from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path("", views.show_subjects),
    path("praise/", views.praise_or_criticize),
    path("criticize/", views.praise_or_criticize),
    path("admin/", admin.site.urls),
    path("api/subjects/", views.show_subjects),
    path("api/teachers/", views.show_teachers),
]
