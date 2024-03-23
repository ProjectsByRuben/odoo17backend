# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'

    _description = "Library Book Model"

    name = fields.Char(
        string="Name",
    )

    isbn = fields.Char(string="ISBN", size=9)
    date = fields.Date(string="Publication Date")
    image = fields.Image()
    stage_id = fields.Many2one(
        "library.book.stage", string="Stage")
    author_id = fields.Many2one(
        "library.author", string="Author")
    pages = fields.Integer(string="Pages")
    description = fields.Html(string="Description")
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
        store=True)
    price = fields.Monetary(string="Price")
    comments = fields.Text(string="Comments")
