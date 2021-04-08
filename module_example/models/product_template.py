# _*_ coding: utf-8 _*_

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_session_product = fields.Boolean(string='Use as session product',
                                        help='check this box to use session',
                                        default=True)
    _name = 'test.product_template'
    _description = 'course info modify'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='this is a very long title')
    level = fields.Selection(string='level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advance', 'Advance')
                                        ],
                             copy=False)
