import datetime
from odoo import fields, models


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date('Birthday')
    is_trainee_access = fields.Boolean('Has trainee access?',
                                       compute="_compute_access_trainee")

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)

    def _compute_access_trainee(self):
        self.ensure_one()
        return self.create_date > datetime.now() - datetime.timedelta(days=30)
