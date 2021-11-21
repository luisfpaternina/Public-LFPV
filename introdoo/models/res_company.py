from odoo import models, fields, api, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    terms = fields.Text(string="Terminos y condiciones")
