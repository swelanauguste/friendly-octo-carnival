from django.urls import path

from . import views

app_name = "payroll"

urlpatterns = [
    path("", views.DeductionChangeListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.DeductionChangeDetailView.as_view(), name="detail"),
]
