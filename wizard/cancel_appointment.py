from odoo import fields, models, api


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    reason = fields.Text(string='Reason')

    def cancel_appointment(self):
        pass
