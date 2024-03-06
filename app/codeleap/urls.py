from django.urls import path
from . import views

urlpatterns = [
    path("", views.CodeleapView.as_view(), name='codeleap-list'),
    path(
        "<int:codeleap_id>/",
        views.CodeleapDetailView.as_view(),
        name='codeleap-detail'
    ),
]
