# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    is_split = fields.Boolean(string="Split")

