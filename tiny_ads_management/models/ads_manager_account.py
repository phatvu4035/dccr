from odoo import models, fields

class ConnectionInformation(models.Model):
    _name = 'ads.manager.account'
    _description = 'Marketing Platform Ads Manager Accounts'

    name = fields.Char(
        string="Account Name",
        required=True,
        help="The display name of the Ads Manager Account."
    )

    platform = fields.Selection(
        selection=[
            ('facebook', 'Facebook BM'),
            ('google', 'Google (MCC)'),
            ('tiktok', 'TikTok BC'),
            ('shopee', 'Shopee BM')
        ],
        string="Platform",
        required=True,
        help="Account platform where this Account belongs to."
    )

    account_id = fields.Char(
        string="Account ID",
        required=True,
        help="Unique identifier of the Account (Business Manager ID, MCC ID, BC ID, Shop ID, etc.)."
    )

    email = fields.Char(
        string="Owner Email"
    )

    phone = fields.Char(
        string="Phone Number",
    )

    address = fields.Char(string="Address")


    company_name = fields.Char(
        string="Company Name"
    )

    connection_key = fields.Char(
        string="Connection Key",
        help="Key to connection with this Ads Business Account in Facebook, Business Center in Tiktok, Customer in Google."
    )

    connection_secret = fields.Char(
        string="Connection Secret"
    )
