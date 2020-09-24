from odoo import fields, models


class Rproduct(models.Model):
    _name = "rproduct"
    _description = "Store product"

    name = fields.Char("Store")
