from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:quesion_id>/", views.detail, name="detail"),
    path("int:quesion_id>/results", views.results, name="results"),
    path("int:quesion_id>/vote", views.vote, name="vote"),

]