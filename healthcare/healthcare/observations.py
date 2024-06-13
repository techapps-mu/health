import csv
import frappe

def import_observation_templates_from_csv():
    file_path = '/Users/tzhost13m1/wrk/msconsult/frappe-bench/apps/healthcare/healthcare/data/observations.csv'
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            observation_template = frappe.get_doc({
                "doctype": "Observation Template",
                "observation": row["Reference Range"],
                "description": row["Description"],
                "observation_category": 'Laboratory', #row["Category"],
                "parameters": [
                    {
                        "parameter": row["Parameter"],
                        "units": row["Units"],
                        "reference_range": row["Reference Range"],
                        "normal_range": row["Normal Range"],
                        "abnormal_range": row["Abnormal Range"]
                    }
                ]
            })
            observation_template.insert(ignore_permissions=True)

if __name__ == "__main__":
    import_observation_templates_from_csv()