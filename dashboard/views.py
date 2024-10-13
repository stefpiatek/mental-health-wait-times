from django.shortcuts import render
from .models import Pathway


def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")


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

    return render(request, "dashboard/summary.html", context=context)


def all_patients_view(request):

    pathway_data = Pathway.objects.all()

    context = {"pathway_data": pathway_data}

    return render(request, "dashboard/all_patients.html", context=context)
