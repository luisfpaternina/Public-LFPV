# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerTown(models.Model):
    _name = 'res.partner.town'
    _inherit = 'mail.thread'
    _description = 'Patients'

    name = fields.Char(
        string="Name",
        tracking=True)
