import csv
import frappe
from frappe.utils import cstr

def add_medication_classes():
    medication_classes = [
        "Analgesic",
        "NSAID",
        "Antibiotic",
        "Antidiabetic",
        "Statin",
        "Proton Pump Inhibitor",
        "ACE Inhibitor",
        "Thyroid Hormone",
        "Calcium Channel Blocker",
        "Beta Blocker",
        "Bronchodilator",
        "Diuretic",
        "Leukotriene Receptor Antagonist",
        "Corticosteroid",
        "Anticonvulsant",
        "Antidepressant",
        "Insomnia",
        "Benzodiazepine",
        "Muscle Relaxant"
    ]

    for medication_class in medication_classes:
        if not frappe.db.exists('Medication Class', medication_class):
            doc = frappe.get_doc({
                'doctype': 'Medication Class',
                'medication_class': medication_class
            })
            doc.insert()
            frappe.db.commit()



def add_uoms():
    uoms = [
        "mg",
        "mcg",
        "%",
        "g"
    ]

    for uom in uoms:
        if not frappe.db.exists('UOM', uom):
            doc = frappe.get_doc({
                'doctype': 'UOM',
                'uom_name': uom
            })
            doc.insert()
            frappe.db.commit()


def import_medications():
    file_path = '/Users/tzhost13m1/wrk/msconsult/frappe-bench/apps/healthcare/healthcare/data/medications.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            if not frappe.db.exists('Medication', {'medication_name': row['Medication Name']}):
                doc = frappe.get_doc({
                    'doctype': 'Medication',
                    'medication_name': cstr(row['Medication Name']),
                    'generic_name': cstr(row['Generic Name']),
                    'dosage_form': 'Capsule',#cstr(row['Dosage Form']),
                    'strength': cstr(row['Strength']),
                    'medication_class': 'Diuretic',#cstr(row['Medication Class']),
                    'abbr': cstr(row['Abbr']),
                    'strength_uom': cstr(row['Strength UOM']),
                    'default_prescription_dosage':  'Once Daily', #cstr(row['Default Prescription Dosage']),
                    'default_prescription_duration': '1 Day' #cstr(row['Default Prescription Duration'])
                })
                
                doc.insert()
                frappe.db.commit()

if __name__ == "__main__":
    import_medications()
