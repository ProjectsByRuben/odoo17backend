# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'

    _description = "Library Book Model"

    name = fields.Char(
        string="Book",
        size=20,
    )

    date = fields.Date(string="Date")

    image = fields.Image()

    stage_id = fields.Many2one(
        "library.book.stage", string="Stage")

    author_id = fields.Many2one(
        "library.author", string="Author")
