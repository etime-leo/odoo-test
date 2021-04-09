from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    _name = 'test.sale.wizard'
    _description = 'wizard: quick install'

    def _default_session(self):
        return self.env['test.session'].browse(self.context.get('active_id'))

    session_id = fields.Many2one(comodel_name='test.session',
                                 string='session',
                                 required=True,
                                 default=_default_session)

    session_student_id = fields.Many2many(comodel_name='res.partner',
                                          string='Student in current session',
                                          related='session_id.student_ids',
                                          helps='bla bla')

    student_ids = fields.Many2many(comodel_name='res.partner',
                                  string='Student for sale')

    def create_sale_order(self):

        session_product_id = self.env['product.product'].search([{'is_session_product','=',True}], limit=1)
        if session_product_id:
            for student in self.student_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id': student.id,
                    'session_id': self.session.id,
                    'order_line': [{0,0,{'product_id':session_product_id.id, 'price_unit': self.session_id.total_price}}]
                })