from odoo import models, fields, api
from datetime import date, time, datetime

class MyWizard(models.TransientModel):
    _name = 'inventory.stock.report.wiz'
    _description = 'Inventory Stock Report Wizard'
    product_id = fields.Many2many("product.product",string="Products")
    date = fields.Date(string='Historical Date', default=fields.Date.today)
    on_hand_stock = fields.Float(string='On Hand Stocks')
    def action_get_record(self):
        self.env["data.storage.wiz"].search([]).unlink()
        datatime_obj = datetime.combine(self.date, time(0, 0, 0))

        stock_in_records = self.env['stock.move.line'].search([
            ('product_id', 'in', self.product_id.ids),
            ('state', '=', 'done'),
            ('location_id.usage', '!=', 'internal'),
            ('location_dest_id.usage', '=', 'internal'),
            ('date', '<=', datatime_obj)
        ])

        # total_in = sum(stock_in_records.mapped('quantity'))
        stock_out_records = self.env['stock.move.line'].search([
            ('product_id', 'in', self.product_id.ids),
            ('state', '=', 'done'),
            ('location_id.usage', '=', 'internal'),
            ('location_dest_id.usage', '!=', 'internal'),
            ('date','<=',datatime_obj)
        ])
        for p in self.product_id:
            current_product_stock_in = sum(stock_in_records.filtered(lambda r: r.product_id.id == p.id).mapped('quantity'))
            current_product_stock_out = sum(stock_out_records.filtered(lambda r: r.product_id.id == p.id).mapped('quantity'))
            # lines.update({"product_id":p.id,"on_hand_stock":current_product_stock_in - current_product_stock_out})
            print(self.date)
            print(p.id)
            print((current_product_stock_in - current_product_stock_out))
            self.env["data.storage.wiz"].create({
                "date":self.date,
                "product_id":p.id,
                "on_hand_stock":(current_product_stock_in - current_product_stock_out)})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Data Storage Wizard',
            'res_model': 'data.storage.wiz',
            'view_mode': 'tree',
            'target': 'new',
        }


