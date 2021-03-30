# noinspection PyStatementEffect
{
    'name': 'Module Example',
    'summary': 'Example of the module',
    'description': '*',
    'author': 'me',
    'website': 'https://etime-leo-odoo-test-develop-2294612.dev.odoo.com/',
    'category': 'training',
    'version': '0.1',
    'depends': ['base'],
    'date': [
        'security/test_security.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/test_menuitems.xml',
    ],
    'demo': [
        'demo_data/course_demo.xml',
        'demo_data/spaceship_demo.xml',
    ],

}
