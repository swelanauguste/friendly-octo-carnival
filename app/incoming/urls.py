from django.urls import path

from . import views

app_name = "incoming"

urlpatterns = [
    path("add/", views.IncomingCreateView.as_view(), name="create"),
    path("detail/<slug:slug>/", views.IncomingDetailView.as_view(), name="detail"),
]
