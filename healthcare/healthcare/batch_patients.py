import frappe
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Function to generate a random patient
@frappe.whitelist()
def generate_patient():
    email = fake.email()
    mobile = fake.basic_phone_number()
    uid = fake.uuid4()
    # Using a service like 'loremflickr' to generate random image URLs
    image = f'https://loremflickr.com/320/240/person?random={fake.random_number()}'

    first_name = fake.first_name()
    last_name = fake.last_name()

    patient = {
        # 'doctype': 'Patient',
        'first_name': first_name,
        'last_name': last_name,
        'name': f'{first_name} {last_name} {uid[:5]}',
        'sex': 'Female' if fake.passport_gender() == 'F' else 'Male',
        'email': email,
        'mobile': mobile,
        'uid': uid,
        'image': image
    }
    return patient

# Generate 1000 patients
patients = [generate_patient() for _ in range(1000)]

# Extract fields and values for bulk insert
fields = list(patients[0].keys())
values = [tuple(patient.values()) for patient in patients]

# Batch insert patients into Frappe
def batch_insert_patients(fields, values):
    frappe.db.bulk_insert('Patient', fields=fields, values=values)
    frappe.db.commit()

# Execute the batch insertion
batch_insert_patients(fields, values)

print("Successfully created 1000 patients.")