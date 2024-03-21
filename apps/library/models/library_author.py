# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = 'library.author'

    _description = "Library author Model"

    name = fields.Char(
        string="author",
        size=20,
    )
