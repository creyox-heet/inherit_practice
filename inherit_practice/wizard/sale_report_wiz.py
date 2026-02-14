from odoo import fields, models
class SaleReportWiz(models.TransientModel):
    _name = 'sale.report.wiz'
    _description = "Sale Report Wizard"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    customer_id = fields.Many2one('res.partner', string="Customer")

    def action_get_sale_report_data(self):
        self.ensure_one()
        orders = self.env['sale.order'].search([('partner_id','=',self.customer_id.id),('date_order','>=',self.start_date),('date_order','<=',self.end_date)])
        print(orders)
        return orders
    def action_download_pdf_report(self):
        self.ensure_one()
        return self.env.ref("inherit_practice.action_sale_report_template").report_action(self)