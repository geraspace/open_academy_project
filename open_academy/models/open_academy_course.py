
from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "open.academy.course.description"

    name = fields.Char(string="Course", required=True)
    description = fields.Text(string="Course description", required=True)
