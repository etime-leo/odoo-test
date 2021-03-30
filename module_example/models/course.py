# _*_ coding: utf-8 _*_

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):
    _name = 'test.course'
    _description = 'course info modify'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='this is a very long title')
    level = fields.Selection(string='level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advance', 'Advance')
                                        ],
                             copy=False)

    active = fields.Boolean(string='Active', default=True)

    base_price = fields.Float(string='base price', default=0.00)

    additional_fee = fields.Float(string='add fee', default=10.00)

    total_price = fields.Float(string='Tototal price', readonly=True)

    @api.onchange('base price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base price sux')
        self.total_price = self.base_price + self.additional_fee

    @api.constraint('addition_fee')
    def _check_addition_fee(self):
        for record in self:
            if record.addition_fee < 10.00:
                raise ValidationError(f'addition fiel sux: {record.addition_fee}')