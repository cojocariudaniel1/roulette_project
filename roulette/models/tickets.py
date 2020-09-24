from odoo import api, exceptions, fields, models


class Tickets(models.Model):
    _name = "test13_ticket"
    _description = "Tickets"
    _inherit = "test13_client"

    active = fields.Boolean(default=True)
    text = fields.Char(default="Buy a ticket:")
    name = fields.Char("Ticket ID", store=True, default="New code")

    price = fields.Integer()

    @api.constrains("price")
    def _check_price(self):
        if self.price == 0:
            raise exceptions.ValidationError("Price can't be zero !!")
        if self.price < 0:
            raise exceptions.ValidationError("Price can't be negative !!")

    date = fields.Date(string="Date", default=lambda self: fields.Date.today())

    @api.model
    def create(self, vals):
        if vals.get("name", "New code") == "New code":
            vals["name"] = self.env["ir.sequence"].next_by_code("self.service") or "New code"
        result = super(Tickets, self).create(vals)
        return result

    number_1 = fields.Integer(required=True, default="")
    number_2 = fields.Integer(required=True, default="")
    number_3 = fields.Integer(required=True, default="")
    number_4 = fields.Integer(required=True, default="")
    number_5 = fields.Integer(required=True, default="")
    number_6 = fields.Integer(required=True, default="")

    @api.constrains("number_1", "number_2", "number_3", "number_4", "number_5", "number_6")
    def _check_numbers(self):
        if (
            (self.number_1 > 49)
            or (self.number_2 > 49)
            or (self.number_3 > 49)
            or (self.number_4 > 49)
            or (self.number_5 > 49)
            or (self.number_6 > 49)
        ):
            raise exceptions.ValidationError("Numbers must not be above 49 !!")
        if (
            (self.number_1 < 1)
            or (self.number_2 < 1)
            or (self.number_3 < 1)
            or (self.number_4 < 1)
            or (self.number_5 < 1)
            or (self.number_6 < 1)
        ):
            raise exceptions.ValidationError("Numbers must not be zero or negative !!")

    result = fields.Integer(string="Result")

    status_unextracted = fields.Char(string="Status", default="Unextracted")
    status_extracted = fields.Char(default="Extracted")
