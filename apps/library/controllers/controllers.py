# -*- coding: utf-8 -*-
# from odoo import http


# class ../extra-addons/odoo17backend/apps/library(http.Controller):
#     @http.route('/../extra-addons/odoo17backend/apps/library/../extra-addons/odoo17backend/apps/library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../extra-addons/odoo17backend/apps/library/../extra-addons/odoo17backend/apps/library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('../extra-addons/odoo17backend/apps/library.listing', {
#             'root': '/../extra-addons/odoo17backend/apps/library/../extra-addons/odoo17backend/apps/library',
#             'objects': http.request.env['../extra-addons/odoo17backend/apps/library.../extra-addons/odoo17backend/apps/library'].search([]),
#         })

#     @http.route('/../extra-addons/odoo17backend/apps/library/../extra-addons/odoo17backend/apps/library/objects/<model("../extra-addons/odoo17backend/apps/library.../extra-addons/odoo17backend/apps/library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../extra-addons/odoo17backend/apps/library.object', {
#             'object': obj
#         })

