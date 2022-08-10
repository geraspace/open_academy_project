from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpenAcademySession(models.Model):
    _name = "open.academy.session"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)

    instructor_id = fields.Many2one("res.partner", domain=["|", ("instructor", "=", "True"),
                                    ("category_id", "child_of", "Teacher")])
    course_id = fields.Many2one("open.academy.course", ondelete="cascade", required=True)
    attendee_ids = fields.Many2many("res.partner", "session_res_partner_rel", string="Attendes")

    attendees_count = fields.Integer(compute='_compute_attendees_count', store=True)
    taken_seats = fields.Float(compute="_compute_taken_seats")

    @api.depends("attendee_ids")
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)

    @api.depends("seats", "attendee_ids")
    def _compute_taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange("seats", "attendee_ids")
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                "warning": {
                    "title": "Incorrect values",
                    "message": "The number of seats can not be less than 0."
                }
            }
        if len(self.attendee_ids) > self.seats:
            return {
                "warning": {
                    "title": "Incorrect values",
                    "message": "The number of attendees can not be greater than the seats available."
                }
            }

    @api.constrains("instructor_id", "attendee_ids")
    def _check_instructor_in_attendee(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee.")
