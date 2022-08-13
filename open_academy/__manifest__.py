{
    "name": "Open Academy",
    "summary": """
        Module description""",
    "author": "Vauxoo",
    "website": "https://www.odoo.com/",
    "category": "Test module",
    "license": "LGPL-3",
    "version": "15.0.1.0.1",
    "depends": [
        "board"
        ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/open_academy_course_views.xml",
        "views/open_academy_session_views.xml",
        "views/res_partner_views.xml",
        "views/open_academy_menus_views.xml",
        "views/open_academy_session_board.xml",
        "wizards/open_academy_wizard_views.xml",
        "reports/open_academy_session_report.xml"
        ],
    "demo": [
        "demo/open_academy_course_demo.xml"
    ],
}
