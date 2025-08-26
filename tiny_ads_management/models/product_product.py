from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = "product.product"

    expense_type = fields.Selection(
        selection=[
            ("ads_account_expense", "Ads Account Expense"),
            ("ads_campaign_expense", "Ads Campaign Expense"),
        ],
        string="Expense Type",
        help="Classify the product for expense reporting:\n"
             "- Ads Expense: Costs related to running advertisements (e.g., Facebook Ads, Google Ads).\n"
             "- Campaign Expense: Costs associated with broader marketing campaigns (e.g., event organization, influencer fees).")
