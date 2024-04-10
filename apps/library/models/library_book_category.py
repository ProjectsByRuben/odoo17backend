# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import UserError


class BookCategory(models.Model):
    _name = "library.book.category"

    _description = "Library Book category Model"

    name = fields.Char(
        string="Category Name",
        size=20,
    )

    color = fields.Integer(string="Color")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_master_category(self):
        master_xmlids = [
            "library_book_category_1",
        ]
        for master_xmlid in master_xmlids:
            master_tag = self.env.ref(
                f"library.{master_xmlid}", raise_if_not_found=False
            )
            if master_tag and master_tag in self:
                raise UserError("No puedes eliminar esta Categoria!")
