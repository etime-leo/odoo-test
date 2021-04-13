# _*_ coding: utf-8 _*_

from odoo import models, fields, api


class Spaceship(models.Model):
    _name = 'test.spaceship'
    _description = 'This is the spaceship of the exercise 1'

    name = fields.Char(string='name', required=True)
    description = fields.Text(string='this is a very long title')
    dimension = fields.Float('feet', digits=(12,2))
    fuel = fields.Float('gallons', digits=(12,1))
    n_passenger = fields.Integer('passenger')
    ship_type = fields.Selection(string='type',
                                 selection=[('small', 'Sidewinder'),
                                            ('medium', 'Cobra MK IV'),
                                            ('large', 'Python')
                                            ],
                                 copy=False)
    active = fields.Boolean(string='Active', default=True)
