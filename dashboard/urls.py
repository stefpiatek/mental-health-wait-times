from django.urls import path
from .views import dashboard_view, summary_view, all_patients_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("summary", summary_view, name="summary"),
    path("all_patients", all_patients_view, name="all_patients"),
]
