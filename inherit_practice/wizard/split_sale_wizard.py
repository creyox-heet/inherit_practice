from odoo import fields, models
class SplitSaleWizard(models.TransientModel):
   _name = 'split.sale.wiz'
   _description = "Split Sale Wizard"
   partner_id = fields.Many2one('res.partner', string="Partner")

   # def action_for_split(self):
   #    if self.partner_id:
   #       self.env["sale.order.line"].search(['is_split', '=', True)])
   #
