# -*- coding: utf-8 -*-
# from odoo import http


# class DemoReports(http.Controller):
#     @http.route('/demo_reports/demo_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_reports/demo_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_reports.listing', {
#             'root': '/demo_reports/demo_reports',
#             'objects': http.request.env['demo_reports.demo_reports'].search([]),
#         })

#     @http.route('/demo_reports/demo_reports/objects/<model("demo_reports.demo_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_reports.object', {
#             'object': obj
#         })
