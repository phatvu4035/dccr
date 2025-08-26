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
    description = fields.Char(string="Page Description")
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

    url = fields.Char(
        string="Page URL",
        help="The full URL to the page."
    )
    profile_picture_url = fields.Char(string="Profile Picture URL")

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

    # -------------------------
    # Status & Meta
    # -------------------------
    state = fields.Selection(
        [
            ("active", "Active"),
            ("inactive", "Inactive"),
        ],
        string="Verification Status",
        help="Verification status of the page."
    )
    created_time = fields.Datetime(
        string="Created Time",
        help="The date and time when the page was created."
    )
