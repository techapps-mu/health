import csv
import frappe
from frappe.utils import cstr



def import_medications():
    file_path = '/Users/tzrootm1mi/wrk/msconsult/frappe-bench/apps/healthcare/healthcare/data/meds.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        values = []
        keys = {}
        for row in reader:
            med_name = row.get('med_name')
            if med_name and keys.get(med_name) is None:
                values.append((med_name,med_name))
                keys[med_name] = True
        
        
        frappe.db.bulk_insert('Med', fields=['med_name', 'name'], values=values)
        frappe.db.commit()

if __name__ == "__main__":
    import_medications()
