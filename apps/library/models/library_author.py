# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = 'library.author'

    _description = "Library author Model"

    name = fields.Char(
        string="Author",
        size=20,
    )

    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name="author_id",
        string="Books")

    image = fields.Image()
