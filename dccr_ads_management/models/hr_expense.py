from odoo import models, fields

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    bill_id = fields.Char(string="Bill ID", help="Unique identifier of the invoice, usually provided by the advertising platform.")
    ad_account_id = fields.Many2one("ads.account", string="Ads Account")
    due_date = fields.Datetime(string="Due Date", help="The date when the advertising invoice was due.")
