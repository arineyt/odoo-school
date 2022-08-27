from odoo import fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library books category'

    name = fields.Char()
    active = fields.Boolean(default="True")

    book_ids = fields.One2many(
        comodel_name="library.book",
        inverse_name="category_id"
    )
