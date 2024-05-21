// Copyright (c) 2024, earthians Health Informatics Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gynae Consultation", {
  patient(frm) {
    const patientContainer = $("[data-fieldname='patient_details']");
    patientContainer.removeClass("hide-control");

    patientContainer
      .empty()
      .append(frappe.render_template("gynae_patient", {}));
  },
  refresh(frm) {
    console.log("refresh", frm.doc.patient);
  },
});
