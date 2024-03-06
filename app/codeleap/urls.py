from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserView.as_view()),
    path("<int:user_id>/", views.UserDetailView.as_view()),
]
