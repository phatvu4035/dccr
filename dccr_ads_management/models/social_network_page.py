from odoo import models, fields


class SocialNetworkPage(models.Model):
    _name = "social.network.page"
    _description = "Social Network Page"

    # -------------------------
    # Basic Identification
    # -------------------------
    name = fields.Char(
        string="Page Name",
        required=True,
        help="The display name of the page on the social network."
    )
    page_id = fields.Char(
        string="Page ID",
        required=True,
        index=True,
        help="Unique identifier of the page from the social platform (e.g. Facebook Page ID)."
    )
    platform = fields.Selection(
        [
            ("facebook", "Facebook"),
            ("google", "Google Business Profile"),
            ("shopee", "Shopee"),
            ("tiktok", "tiktok"),
        ],
        string="Platform",
        required=True,
        help="The social network or platform where this page exists."
    )

    ad_account_id = fields.Many2one(
        "ads.account",
        string="Account ID",
        required=True
    )

    link = fields.Char(
        string="Page URL",
        help="The full URL to the page."
    )

    # -------------------------
    # Contact & Location
    # -------------------------
    phone = fields.Char(
        string="Phone Number",
        help="Business contact phone number."
    )
    email = fields.Char(
        string="Email",
        help="Business email address."
    )
    website = fields.Char(
        string="Website",
        help="Website linked to the page."
    )
    address = fields.Char(
        string="Address",
        help="Street address of the business."
    )
    city = fields.Char(
        string="City",
        help="City where the business is located."
    )
    country = fields.Char(
        string="Country",
        help="Country where the business is located."
    )
    zip_code = fields.Char(
        string="Zip Code",
        help="Postal code of the business location."
    )

    # -------------------------
    # Page Info & Stats
    # -------------------------
    # category = fields.Char(
    #     string="Category",
    #     help="Primary category of the page (e.g. Retail, Education)."
    # )
    # fan_count = fields.Integer(
    #     string="Fans / Likes",
    #     help="Total number of fans or likes of the page."
    # )
    # followers_count = fields.Integer(
    #     string="Followers",
    #     help="Total number of followers of the page."
    # )
    # rating_count = fields.Integer(
    #     string="Rating Count",
    #     help="Number of ratings the page has received."
    # )
    # overall_star_rating = fields.Float(
    #     string="Star Rating",
    #     help="Overall average rating of the page (if available)."
    # )

    # -------------------------
    # Status & Meta
    # -------------------------
    is_published = fields.Boolean(
        string="Published",
        help="Whether the page is currently published."
    )
    verification_status = fields.Selection(
        [
            ("verified", "Verified"),
            ("unverified", "Unverified"),
            ("in_progress", "Verification in Progress"),
        ],
        string="Verification Status",
        help="Verification status of the page."
    )
    created_time = fields.Datetime(
        string="Created Time",
        help="The date and time when the page was created."
    )
