from django.urls import path
from . import views

app_name = "meninoDjango"

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "landingpage/",
        views.landingpage,
        name="landingpage"
    ),

    path(
        "vote/<int:question_id>/",
        views.vote,
        name="vote"
    ),

    path(
        "results/<int:question_id>/",
        views.results,
        name="results"
    ),
]