from odoo import models, fields

class AdsBusinessAccount(models.Model):
    _name = 'ads.business.account'
    _description = 'Advertising Business Account'

    name = fields.Char(
        string="Account Name",
        required=True,
        help="The display name of the Business Account."
    )

    business_id = fields.Char(
        string="Business/Manager ID",
        required=True,
        help="Unique identifier of the Business Account (Business Manager ID, MCC ID, BC ID, Shop ID, etc.)."
    )

    account_email = fields.Char(
        string="Owner Email",
        help="Email address associated with the Business Account."
    )

    phone = fields.Char(
        string="Phone Number",
    )

    address = fields.Char(string="Address")

    platform = fields.Selection(
        selection=[
            ('facebook', 'Facebook Business Account'),
            ('google', 'Google Ads Manager (MCC)'),
            ('tiktok', 'TikTok Business Center'),
            ('shopee', 'Shopee Business Account'),
        ],
        string="Platform",
        required=True,
        help="Advertising platform where this Business Account belongs to."
    )

    company_name = fields.Char(
        string="Company Name",
        help="Company Name associated with this Business Account."
    )

    api_key = fields.Char(
        string="API Key / Token",
        help="Access token or API key used for integration with the platform."
    )

    status = fields.Selection(
        selection=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('suspended', 'Suspended'),
        ],
        string="Status",
        default='active',
        help="Current status of the Business Account."
    )

