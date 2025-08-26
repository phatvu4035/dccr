from odoo import models, fields

class PageCategory(models.Model):
    _name = 'page.category'

    name = fields.Char('Page Category', required=True)
