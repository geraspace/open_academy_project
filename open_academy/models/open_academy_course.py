from odoo import models, fields, api


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "open.academy.course"

    name = fields.Char(string="Course", required=True)
    description = fields.Text(required=True)
    responsible_id = fields.Many2one('res.users')
    session_ids = fields.One2many('open.academy.session', 'course_id')

    _sql_constraints = [
        ('name_description',
         'CHECK(name != description)',
         "The course title must be different to the description."),
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique."),
    ]

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get("name"):
            default["name"] = "Copy of " + self.name
        return super().copy(default)
