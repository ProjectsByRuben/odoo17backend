# -*- coding: utf-8 -*-

import logging
from odoo import _, api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    transactions_count = fields.Integer(
        string="Total Done",
        copy=False,
        compute="_compute_transactions_count")
    transaction_done_ids = fields.Many2many(
        comodel_name='payment.transaction',
        string="Done Transactions",
        help="Show Done Transactions",
        compute='_compute_done_transaction_ids',
        copy=False,
        compute_sudo=True
    )

    @api.depends('transaction_ids')
    def _compute_transactions_count(self):
        for tr in self:
            tr.transactions_count = len(tr.transaction_ids)

    @api.depends('transaction_ids')
    def _compute_done_transaction_ids(self):
        for trans in self:
            trans.transaction_done_ids = trans.transaction_ids.filtered(
                lambda t: t.state == 'done')

    def action_view_transactions(self):
        res_action = {
            'name': _('Payments'),
            'type': 'ir.actions.act_window',
            'res_model': 'payment.transaction',
            'target': 'current',
        }
        payments = self.transaction_ids.ids
        if len(payments) == 1:
            res_action['res_id'] = payments[0]
            res_action['view_mode'] = 'form'
        else:
            res_action['view_mode'] = 'tree,form'
            res_action['domain'] = [('id', 'in', payments)]
        return res_action
