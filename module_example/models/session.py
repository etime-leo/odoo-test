# _*_ coding: utf-8 _*_

from odoo import models, fields, api


class Session(models.Model):
    _name = 'test.session'
    _description = 'session info'

    course_id = fields.Many2one(comodel_name='test.course',
                                string='Course',
                                ondelete='cascade',
                                required=True)

    name = fields.Char(string='Title', related='course_id.name')

    # res.partner already imported from odoo source code
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')

    student_ids = fields.Many2many(comodel_name='res.partner', string='Student')
