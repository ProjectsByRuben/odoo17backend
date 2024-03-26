# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_domain_payments(self):
        return [('state', '=', 'done')]

    transaction_ids = fields.Many2many(domain=_get_domain_payments)
