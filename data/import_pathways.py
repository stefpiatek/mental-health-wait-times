import json
import csv
from datetime import datetime as dt


csv_file_path = "pathway_data.csv"
json_data = []
original_format = "%d/%m/%y"
desired_format = "%Y-%m-%d"

# Read in file
with open(csv_file_path, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["triage_date"] == "":
            row["triage_date"] = None
        if row["first_contact_date"] == "":
            row["first_contact_date"] = None
            row["clinician"] = None
            row["pathway_type"] = None
        else:
            row["clinician"] = int(row["clinician"])
            row["pathway_type"] = int(row["pathway_type"])

        json_data.append(
            {
                "model": "dashboard.pathway",
                "pk": int(row["patient"]),
                "fields": {
                    "patient": int(row["patient"]),
                    "referral_date": row["referral_date"],
                    "triage_date": row["triage_date"],
                    "pathway_type": row["pathway_type"],
                    "urgent": int(row["urgent"]),
                    "first_contact_date": row["first_contact_date"],
                    "clinician": row["clinician"],
                },
            }
        )

# Export as JSON
json_file_path = "output.json"
with open(json_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"Converted '{csv_file_path}' to '{json_file_path}' successfully.")
