from odoo import fields, models
class SplitSaleWizard(models.TransientModel):
   _name = 'split.sale.wiz'
   _description = "Split Sale Wizard"

   partner_id = fields.Many2one('res.partner', string="Partner")

   def action_for_split(self):
      self.ensure_one()
      # print(self.partner_id)
      # print(self.env.context.get("form_partner_id"))
      if self.partner_id:
         current_form_partner_id = self.env.context.get("form_partner_id")
         # print(current_form_partner_id)
         temp = self.env['sale.order'].search([('partner_id','=',current_form_partner_id)])
         order_lines = []
         for i in temp.order_line:
            order_lines.append(i.id)
         print(order_lines)
         split_order_lines = self.env['sale.order.line'].search([('id','in',order_lines),('is_split','=',True)])
         new_record1 = self.env['sale.order'].create({'partner_id':self.partner_id.id ,'order_line': split_order_lines})
         print(new_record1)

