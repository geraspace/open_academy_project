from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = "open.academy.wizard"
    _description = "open.academy.wizard"

    session_ids = fields.Many2many(
        'open.academy.session',
        default=lambda self: self._default_sessions())
    attendee_ids = fields.Many2many("res.partner")

    def _default_sessions(self):
        return self.env["open.academy.session"].browse(self._context.get("active_ids"))

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
