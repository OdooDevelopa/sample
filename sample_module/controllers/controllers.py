# -*- coding: utf-8 -*-
from odoo import http

# class Sample(http.Controller):
#     @http.route('/sample/sample/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample/sample/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample.listing', {
#             'root': '/sample/sample',
#             'objects': http.request.env['sample.sample'].search([]),
#         })

#     @http.route('/sample/sample/objects/<model("sample.sample"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample.object', {
#             'object': obj
#         })