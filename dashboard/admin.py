from django.contrib import admin
from .models import Patient, PathwayType, Clinician, Pathway


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["name", "date_of_birth"]


@admin.register(PathwayType)
class PathwayTypeAdmin(admin.ModelAdmin):
    list_display = ["pathway_type"]


@admin.register(Clinician)
class ClinicianAdmin(admin.ModelAdmin):
    list_display = ["name", "get_specialties"]

    def get_specialties(self, obj):
        return ", ".join([p.pathway_type for p in obj.pathway_type.all()])


@admin.register(Pathway)
class PathwayAdmin(admin.ModelAdmin):
    list_display = [
        "patient",
        "referral_date",
        "triage_date",
        "pathway_type",
        "urgent",
        "first_contact_date",
        "clinician",
    ]
