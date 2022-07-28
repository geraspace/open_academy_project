from odoo import models, fields

class OpenAcademySession(models.Model):
    _name = "open.academy.session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one("res.partner")
    course_id = fields.Many2one("open.academy.course", ondelete="cascade", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Attendes")
