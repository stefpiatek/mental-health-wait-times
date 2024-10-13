from django.shortcuts import render
from .models import Pathway
from django.db.models import Q
from datetime import datetime


def dashboard_view(request):

    # Data from Model
    pathway_data = Pathway.objects.all()

    urgent_referral_dates = pathway_data.filter(
        Q(first_contact_date=None) & Q(urgent=True)
    ).values_list("referral_date", flat=True)
    urgent_wait_days = []
    for date in urgent_referral_dates:
        urgent_wait_days.append((datetime.today().date() - date).days)

    routine_referral_dates = pathway_data.filter(
        Q(first_contact_date=None) & Q(urgent=False)
    ).values_list("referral_date", flat=True)
    routine_wait_days = []
    for date in routine_referral_dates:
        routine_wait_days.append((datetime.today().date() - date).days)

    actual_wait_times = {
        "urgent": urgent_wait_days,
        "routine": routine_wait_days,
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

    urgent_referral_dates = pathway_data.filter(
        Q(first_contact_date=None) & Q(urgent=True)
    ).values_list("referral_date", flat=True)
    urgent_wait_days = []
    for date in urgent_referral_dates:
        urgent_wait_days.append((datetime.today().date() - date).days)

    routine_referral_dates = pathway_data.filter(
        Q(first_contact_date=None) & Q(urgent=False)
    ).values_list("referral_date", flat=True)
    routine_wait_days = []
    for date in routine_referral_dates:
        routine_wait_days.append((datetime.today().date() - date).days)

    context = {
        "urgent": urgent_wait_days,
        "routine": routine_wait_days,
    }

    return render(request, "dashboard/summary.html", context)


def all_patients_view(request):

    pathway_data = Pathway.objects.all().order_by("-referral_date")

    context = {"pathway_data": pathway_data}

    return render(request, "dashboard/all_patients.html", context)
