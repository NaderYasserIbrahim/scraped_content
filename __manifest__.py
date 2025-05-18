{
    'name': 'Scraped Content',
    'version': '1.0',
    'category': 'Custom',
    'description': 'A module to scrape LinkedIn job listings and store them in Odoo.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/scraped_content_views.xml',
        'data/linkedin_jobs.csv',
        'data/techcrunch_blogs.csv',
        'views/scraped_blog_views.xml',
        'views/scraped_page_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
}
