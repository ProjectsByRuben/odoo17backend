# -*- coding: utf-8 -*-

from odoo import models, fields


class BookCategory(models.Model):
    _name = 'library.book.category'

    _description = "Library Book category Model"

    name = fields.Char(
        string="Category Name",
        size=20,
    )
