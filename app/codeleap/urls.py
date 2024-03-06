from django.urls import path
from . import views

urlpatterns = [
    path("https://dev.codeleap.co.uk/careers/", views.CodeleapView.as_view(), name='codeleap-list'),
    path(
        "<int:element_id>/",
        views.CodeleapDetailView.as_view(),
        name='codeleap-detail'
    ),
]
