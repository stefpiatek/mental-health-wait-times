from django.shortcuts import render
from .models import Pathway


def dashboard_view(request):

    # Example hardcoded data for actual wait times
    actual_wait_times = {
        "urgent": [120, 450, 222, 160, 140],
        "routine": [300, 600, 400, 200, 250],
    }

    # Calculate average wait times
    avg_actual_urgent = sum(actual_wait_times["urgent"]) / len(
        actual_wait_times["urgent"]
    )
    avg_actual_routine = sum(actual_wait_times["routine"]) / len(
        actual_wait_times["routine"]
    )

    context = {
        "avg_actual_urgent": avg_actual_urgent,
        "avg_actual_routine": avg_actual_routine,
    }
    return render(request, "dashboard/dashboard.html", context)


def summary_view(request):

    pathway_data = Pathway.objects.all()

    mh_waiting = (
        pathway_data.filter(pathway_type__pathway_type="Mental Health")
        .filter(first_contact_date__isnull=True)
        .count()
    )
    nd_waiting = pathway_data.filter(
        pathway_type__pathway_type="Neurodiversity"
    ).count()

    context = {"mh_waiting": mh_waiting, "nd_waiting": nd_waiting}

    return render(request, "dashboard/summary.html", context)


def all_patients_view(request):

    pathway_data = Pathway.objects.all()

    context = {"pathway_data": pathway_data}

    return render(request, "dashboard/all_patients.html", context)
