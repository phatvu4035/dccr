from odoo import api, models, fields
import pytz

class AdsAccount(models.Model):
    _name = 'ads.account'
    _description = 'Advertising Account (TikTok, Facebook, Shopee, Google)'

    # --- Identification ---
    name = fields.Char("Account Name", required=True, help="Display name of the Ads Account")
    platform = fields.Selection([
        ('facebook', 'Facebook Ads'),
        ('tiktok', 'TikTok Ads'),
        ('shopee', 'Shopee Ads'),
        ('google', 'Google Ads'),
    ], string="Platform", required=True, help="Advertising platform where this account belongs")
    account_id = fields.Char("Account ID", required=True, help="Unique identifier from the platform", )
    ads_manager_account_id = fields.Many2one("ads.manager.account", string="Business Account", help="Business/Manager Account ID (BM, MCC, BC, etc.)")
    state = fields.Selection(selection=[
            ('unauthorised', 'Unauthorised'),
            ('authorised', 'Authorised'),
            ('error', 'Error'),
            ('expired', 'Expired'),
        ],
    string="Status", help="Current status of the ads account")

    currency_id = fields.Many2one("res.currency", string="Currency")
    timezone = fields.Selection(
        selection=[(tz, tz) for tz in pytz.all_timezones],
        string="Timezone",
        default="UTC",
        help="Timezone used for scheduling and displaying date/time information related to this record."
    )
    mapped_expense_ad_account_id = fields.Many2one("tiny.expense.ad.account", string="Expense Ad Account")
    acc_number = fields.Char("Account Number", related="mapped_expense_ad_account_id.acc_number")
    acc_name = fields.Char("Account Name", related="mapped_expense_ad_account_id.acc_name")
    employee_id = fields.Char("Managing Employee", related="mapped_expense_ad_account_id.employee_id")
    possession_type = fields.Char("Possession Type", related="mapped_expense_ad_account_id.possession_type")
    bank_id = fields.Char("Bank", related="mapped_expense_ad_account_id.bank_id")
    marketing_employee_ids = fields.Many2many(string="Marketing Employees", related="mapped_expense_ad_account_id.marketing_employee_ids")

    # --- Campaign ---
    campaign_ids = fields.One2many(
        "ads.campaign", "ad_account_id",
        string="Ads Campaign",
        help="List of running ads campaigns related to this account"
    )

    page_ids = fields.One2many("social.network.page", "ad_account_id",
                               string="Ads Pages",
                               help="List of running ads pages related to this account")

    access_token = fields.Char(
        string="Access Token"
    )

    refresh_token = fields.Char(string="Refresh Token")

    token_expired_date = fields.Datetime(string="Expiration Date")



    # --- Metadata ---
    notes = fields.Text("Notes", help="Internal notes or comments about the account")

    @api.onchange("account_id")
    def _onchange_account_id(self):
        if self.account_id:
            accounts = self.env["tiny.expense.ad.account"].search([("acc_number", "=", self.account_id)])
            if accounts:
                self.mapped_expense_ad_account_id = accounts[0]
