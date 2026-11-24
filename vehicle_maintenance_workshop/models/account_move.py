from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class AccountMove(models.Model):
    _inherit="account.move"

    vehicle_id = fields.Many2one(
        "vehicle.vehicle",
        string = "Veicolo",
        required=True
    )
