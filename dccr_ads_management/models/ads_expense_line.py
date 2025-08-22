from odoo import models, fields

class AdsExpenseLine(models.Model):
    _name = 'ads.expense.line'
    _description = 'Ads Expense Detail Line'

    expense_id = fields.Many2one("hr.expense", string="Expense")
    impressions = fields.Integer("Impressions")
    clicks = fields.Integer("Clicks")
