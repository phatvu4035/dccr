from odoo import models, fields

class AdsExpenseLine(models.Model):
    _name = "ads.expense.line"
    _description = "Ads Expense Detail for Campaign, Ads Account"

    spending_date = fields.Datetime(string="Spending Date")
    campaign_id = fields.Many2one("ads.campaign", string="Campaign")
    spending_amount = fields.Monetary(string="Spending Amount", currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", string="Currency")
