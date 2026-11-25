from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class AccountMove(models.Model):
    _inherit="account.move"

    workorder_id = fields.Many2one(
        "vehicle.workorder",
        string = "Intervento",
        required=True
    )
