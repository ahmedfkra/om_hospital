from datetime import date
from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital patient'

    name = fields.Char(string='Patient Name', tracking=True)
    ref = fields.Char(string='Reference')
    date_of_birth = fields.Date(string='Birth Day')
    age = fields.Integer(string='Age', compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tag')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - self.date_of_birth.year
            else:
                rec.age = 0
