# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_split(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'split.sale.wiz',
            'view_mode': 'form',
            'target': 'new',
            'context': {'form_partner_id': self.partner_id.id},
        }