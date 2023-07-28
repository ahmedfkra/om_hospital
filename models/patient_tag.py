from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'patient.tag'
    _description = 'Description'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active')
    color = fields.Integer(string='Color')
