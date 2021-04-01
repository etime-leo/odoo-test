# -*- coding utf-8 -*-

{
    "name": "Odoo Academy",
    "summary": """Summary etc etc""",
    "author": "E-time",
    "website": "www.e-time.it",
    "category": "Training",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    "demo": [
        "demo/academy_demo.xml"
    ],
}