from django.urls import path
from resume import views

urlpatterns = [
    path("", views.cv_view, name="cv"),
]

