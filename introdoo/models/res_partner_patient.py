# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerPatient(models.Model):
    _name = 'res.partner.patient'
    _inherit = 'mail.thread'
    _description = 'Patients'

    name = fields.Char(
        string="Name",
        tracking=True)
    code = fields.Char(
        string="Code",
        tracking=True)
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)
    phone = fields.Char(
        string="Phone",
        tracking=True)
    country_id = fields.Many2one(
        'res.country',
        string="Country")
    identification_type = fields.Selection([
        ('cc','Cédula'),
        ('nuip','N.U.I.P'),
        ('ti','Tarjeta identidad'),
        ('ps','Pasaporte')],string="Identification type")
    identification_image = fields.Binary(
        string="Identification")
    town_id = fields.Many2one(
        'res.partner.town',
        string="Town")


    @api.onchange('name')
    def _onchange_name(self):
        self.name = self.name.upper() if self.name else False
