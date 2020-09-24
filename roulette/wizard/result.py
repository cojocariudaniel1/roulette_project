import random

from odoo import fields, models


class Result(models.TransientModel):
    _name = "result_wizard"
    _description = "Wizard"

    def _get_default_tickets(self):
        return self.env["test13_ticket"].browse(self.env.context.get("active_ids"))

    tickets_ids = fields.Many2many("test13_ticket", string="Tickets", default=_get_default_tickets)

    def result_wizard(self):

        random_list = []
        for _i in range(0, 49):
            n = random.randint(0, 49)
            random_list.append(n)

        for record in self:
            if record.tickets_ids:
                for results in record.tickets_ids:

                    number_list = []
                    number_list.append(results.number_1)
                    number_list.append(results.number_2)
                    number_list.append(results.number_3)
                    number_list.append(results.number_4)
                    number_list.append(results.number_5)
                    number_list.append(results.number_6)

                    number_intersection = list(set(random_list) & set(number_list))
                    number_intersection_len = len(number_intersection)

                    if number_intersection_len < 1:
                        final_result = 0
                    else:
                        final_result = results.price * (number_intersection_len * 100)

                    results.result = final_result

                    results.status_unextracted = results.status_extracted
