
from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "Course description"

    name = fields.Char(string="Course Title", required=True)
    description = fields.Text(string="Course description")
