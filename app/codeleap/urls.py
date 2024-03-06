from django.urls import path
from . import views

urlpatterns = [
    path("career/", views.CodeleapView.as_view(), name='codeleap-list'),
    path(
        "career/<int:element_id>/",
        views.CodeleapDetailView.as_view(),
        name='codeleap-detail'
    ),
]
