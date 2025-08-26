from odoo import models, fields

class AdsCampaign(models.Model):
    _name = "ads.campaign"
    _description = "Advertising Campaign"

    # --- Basic Info ---
    name = fields.Char(
        string="Name",
        required=True,
        help="The display name of the advertising campaign."
    )
    description = fields.Text(
        string="Description"
    )
    campaign_id = fields.Char(
        string="External Campaign ID",
        help="Unique campaign ID from the advertising platform (Facebook, Google, TikTok, Shopee)."
    )
    platform = fields.Selection(
        selection=[
            ("facebook", "Facebook Ads"),
            ("google", "Google Ads"),
            ("tiktok", "TikTok Ads"),
            ("shopee", "Shopee Ads"),
        ],
        string="Platform",
        required=True,
        help="Advertising platform where the campaign is running."
    )
    ad_account_id = fields.Many2one(
        comodel_name="ads.account",
        string="Ad Account",
        required=True,
        help="The ad account that owns this campaign. A campaign belongs to only one ad account."
    )

    # --- Campaign Settings ---
    objective = fields.Selection(
        selection=[
            ("awareness", "Awareness"),
            ("traffic", "Traffic"),
            ("engagement", "Engagement"),
            ("leads", "Leads"),
            ("app_promotions", "App Promotions"),
            ("sales", "Sales"),
        ],
        string="Objective",
        help="The marketing objective of this campaign, e.g., traffic, sales, or brand awareness."
    )
    utm_source_id = fields.Many2one("utm.source", string="Source")
    marketing_user_id = fields.Many2one("res.users", _compute="_compute_utm_source_field", string="Marketing User")
    marketing_team_id = fields.Many2one("crm.team", _compute="_compute_utm_source_field", string="Marketing Team")
    marketing_company_id = fields.Many2one("crm.team", _compute="_compute_utm_source_field", string="Marketing Company")
    marketing_brand_id = fields.Many2one("utm.medium", _compute="_compute_utm_source_field", string="MKT Brand")

    company_id = fields.Many2one("res.company", string="Company")
    state = fields.Selection(
        selection=[
            ("active", "Active"),
            ("disabled", "Disabled")
        ],
        string="Status",
        help="Current status of the campaign."
    )

    # --- Budget & Schedule ---
    daily_budget = fields.Monetary(
        string="Daily Budget",
        currency_field="currency_id",
        help="Daily budget allocated for this campaign (in the account’s currency)."
    )
    lifetime_budget = fields.Monetary(
        string="Lifetime Budget",
        currency_field="currency_id",
        help="Total budget allocated for this campaign across its lifetime."
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        required=True,
        default=lambda self: self.env.company.currency_id.id
    )
    start_time = fields.Datetime(
        string="Start Time",
        help="Date and time when the campaign starts running."
    )
    end_time = fields.Datetime(
        string="End Time",
        help="Date and time when the campaign ends. Leave empty for ongoing campaigns."
    )

    # --- Performance Metrics ---
    impressions = fields.Integer(
        string="Impressions",
        help="The total number of times the campaign's ads were displayed."
    )
    clicks = fields.Integer(
        string="Clicks",
        help="The number of times users clicked on the ads in this campaign."
    )
    ctr = fields.Float(
        string="CTR (%)",
        help="Click-through rate of the campaign: (clicks / impressions) * 100."
    )
    spent = fields.Monetary(
        string="Spend",
        currency_field="currency_id",
        help="Total money spent on this campaign."
    )
    cpc = fields.Float(
        string="CPC (Cost per Click)",
        help="Average cost per click = Spend / Clicks."
    )
    cpm = fields.Float(
        string="CPM (Cost per 1000 Impressions)",
        help="Average cost per thousand impressions."
    )
    conversions = fields.Integer(
        string="Conversions",
        help="Number of conversions (sales, leads, or other desired actions)."
    )
    conversion_rate = fields.Float(
        string="Conversion Rate (%)",
        help="Conversion rate = (conversions / clicks) * 100."
    )

    # --- Metadata ---
    created_time = fields.Datetime(
        string="Created Time",
        help="The date and time when the campaign was created on the platform."
    )
    updated_time = fields.Datetime(
        string="Updated Time",
        help="The date and time when the campaign was last updated on the platform."
    )

    def _compute_utm_source_field(self):
        for rec in self:
            if not rec.utm_source_id:
                continue
            rec.marketing_user_id = rec.utm_source_id.marketing_user_id
            rec.marketing_team_id = rec.utm_source_id.marketing_team_id
            rec.marketing_company_id = rec.utm_source_id.marketing_company_id
            rec.marketing_brand_id = rec.utm_source_id.marketing_brand_id

    def _search_marketing_users(self, operator, value):
        marketing_users = self.env['res.users'].search([('name', 'ilike', f"%{value}%")])
        utm_sources = self.env['utm.source'].search([('marketing_user_id', 'in', marketing_users.ids)])
        return [('utm_source_id', 'in', utm_sources.ids)]
