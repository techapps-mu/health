import os
import csv
import frappe
dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'relative/path/to/file/you/want')


def lab_requests():
    print(dirname)
    file_path = os.path.abspath(os.path.join(dirname,'../data/labtests.csv'))
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        values = []
        keys = {}
        for row in reader:
            lab_test_name = row.get('test_name')
            if lab_test_name and keys.get(lab_test_name) is None:
                values.append((lab_test_name,lab_test_name))
                keys[lab_test_name] = True
        
        frappe.db.bulk_insert('LabRequest', fields=['test_name', 'name'], values=values)
        frappe.db.commit()


if __name__ == "__main__":
    lab_requests()