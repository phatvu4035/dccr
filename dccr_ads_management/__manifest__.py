{
    'name': 'DCCR Ads Management',
    'version': '1.0',
    'summary': 'Manage advertising campaigns and track performance',
    'description': """
DCCR Ads Management is a comprehensive module designed to help businesses efficiently manage advertising campaigns. 
Key features include:
- Create and manage campaigns across multiple advertising platforms.
- Track budget, expenses, and performance of each campaign.
- Generate detailed reports on impressions, clicks, and conversions.
- Integrate data from multiple sources for a holistic analysis.
- Schedule ad postings and assign responsible team members.

This module is ideal for marketing teams, agencies, and businesses looking to optimize ad performance and ROI.
""",
    'category': 'Marketing',
    'author': 'DCCR / Phat Vu',
    'website': 'https://dccr.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ads_business_account_views.xml',
        'views/ads_account_views.xml',
        'views/social_network_page_views.xml',
        'views/menu_items.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
