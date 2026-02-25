from odoo import models, fields, api
from datetime import date, time, datetime

class DataStorageWiz(models.TransientModel):
    _name = 'data.storage.wiz'
    _description = 'Data Storage Wiz'
    date = fields.Date(string='Historical Date')
    product_id = fields.Many2one("product.product",string="Products")
    on_hand_stock = fields.Float(string='On Hand Stocks')

