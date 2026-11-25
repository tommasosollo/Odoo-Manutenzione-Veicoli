from odoo import models, fields, api


class Workorder(models.Model):
    _name = "vehicle.workorder.type"
    _description = "Workorder Types Model"

    name = fields.Char(string="Nome")

    ricambi_ids = fields.Many2many(
        comodel_name='product.product',
        string='Ricambi collegati',
        required=True
    )
    