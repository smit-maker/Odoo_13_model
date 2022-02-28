# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo_reports(models.Model):
    _name = 'demo.reports' 
    # _inherit = 'res.partner'  
    # _description = 'demo_reports.demo_reports'


    name = fields.Char('Name')
    comp = fields.Text('Company')
    x = fields.Many2one('res.partner')

class demo_company(models.Model):
    _inherit = 'res.partner'  

    demo = fields.One2many('demo.reports', 'name')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    # comp = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
