from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "open.academy.course.description"

    name = fields.Char(string="Course", required=True)
    description = fields.Text(required=True)

    responsible_id = fields.Many2one('res.users')
    session_ids = fields.One2many('open.academy.session', 'course_id')
