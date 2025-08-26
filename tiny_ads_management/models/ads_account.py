from odoo import models, fields
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
    account_id = fields.Char("Account ID", required=True, help="Unique identifier from the platform")
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
