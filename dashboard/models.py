from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class PathwayType(models.Model):
    pathway_type = models.CharField(max_length=50)

    def __str__(self):
        return self.pathway_type


class Clinician(models.Model):
    name = models.CharField(max_length=250)
    pathway_type = models.ManyToManyField(PathwayType, related_name="clinician")

    def __str__(self):
        return self.name


class Pathway(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    referral_date = models.DateField()
    triage_date = models.DateField(null=True, blank=True)
    pathway_type = models.ForeignKey(
        PathwayType, on_delete=models.PROTECT, null=True, blank=True
    )
    urgent = models.BooleanField(null=True, blank=True)
    first_contact_date = models.DateField(null=True, blank=True)
    clinician = models.ForeignKey(
        Clinician, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return f"{self.patient} pathway"
