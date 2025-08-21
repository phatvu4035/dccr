from odoo import models, fields

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
    business_account_id = fields.Many2one("ads.business.account", string="Business Account", help="Business/Manager Account ID (BM, MCC, BC, etc.)")
    account_status = fields.Selection([
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('disabled', 'Disabled'),
        ('suspended', 'Suspended'),
        ('closed', 'Closed'),
    ], string="Status", default='active', help="Current status of the ads account")
    created_time = fields.Datetime("Created Time", help="Account creation date on the platform")
    updated_time = fields.Datetime("Updated Time", help="Last sync/update date from API")

    # --- Ownership & Contact ---
    business_name = fields.Char("Business Name", help="Registered business name for this ads account")
    owner_name = fields.Char("Owner Name", help="Owner or administrator of the ads account")
    owner_email = fields.Char("Owner Email", help="Primary contact email")
    owner_phone = fields.Char("Owner Phone", help="Primary contact phone number")

    # --- Financial & Billing ---
    currency = fields.Char("Currency", help="Currency used in the ads account (e.g., USD, VND)")
    time_zone = fields.Char("Time Zone", help="Time zone of the account for reporting and billing")
    balance = fields.Float("Balance", help="Current balance of the account")
    total_spent = fields.Float("Total Spent", help="Cumulative ad spend since account creation")
    daily_budget = fields.Float("Daily Budget", help="Default daily budget (if supported by the platform)")
    payment_method = fields.Selection([
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('e_wallet', 'E-Wallet'),
        ('invoice', 'Invoice (Postpaid)'),
        ('other', 'Other'),
    ], string="Payment Method", help="Main payment method linked to the account")
    # billing_account_id = fields.Char("Billing Account ID", help="Billing profile or payment account ID")
    # last_payment_date = fields.Datetime("Last Payment Date", help="Date of last payment made")
    # last_payment_amount = fields.Float("Last Payment Amount", help="Amount of last payment")

    # --- Performance Metrics ---
    # impressions = fields.Integer("Impressions", help="Total number of ad impressions")
    # clicks = fields.Integer("Clicks", help="Total number of ad clicks")
    # ctr = fields.Float("CTR (%)", help="Click-through rate")
    # average_cpc = fields.Float("Average CPC", help="Average cost per click")
    # conversions = fields.Integer("Conversions", help="Number of conversions")
    # conversion_value = fields.Float("Conversion Value", help="Total conversion value")
    # roas = fields.Float("ROAS", help="Return on Ad Spend")

    # --- Compliance & Restrictions ---
    # restricted = fields.Boolean("Restricted", help="Whether the account is under restrictions")
    # suspension_reason = fields.Text("Suspension Reason", help="Reason if the account was suspended or disabled")
    # policy_violations = fields.Text("Policy Violations", help="Details about policy violations on the platform")

    # --- Metadata ---
    notes = fields.Text("Notes", help="Internal notes or comments about the account")
