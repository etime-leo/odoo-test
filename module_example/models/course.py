# _*_ coding: utf-8 _*_

from odoo import models, fields, api


class Course(models.Model):
    _name = 'test.course'
    _description = 'course info modify'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='this is a very long title')
    level = fields.Selection(string='level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermidiet', 'Intermidiet'),
                                        ('advanced', 'Advanced')
                                        ],
                             copy=False)

    active = fields.Boolean(string='Active', default=True)