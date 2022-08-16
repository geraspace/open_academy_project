import xmlrpc.client

url = "http://localhost:8069"
db = "rd-mydb"
username = "admin"
password = "admin"

# Authentication
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Show sessions and seats

session_info = models.execute_kw(db, uid, password, 'open.academy.session',
                                 'search_read', [], {'fields': ['name', 'seats']})

for session_and_seats in session_info:
    print("The session '{}' has {} seats".format(session_and_seats["name"], session_and_seats["seats"]))

# Create a session

course_id = models.execute_kw(db, uid, password, "open.academy.course",
                              'search', [[]], {"limit": 1})[0]

instructor_id = models.execute_kw(db, uid, password, 'res.partner',
                                  'search', [[['instructor', '=', True]]],
                                  {'limit': 1})[0]

attendee_id = models.execute_kw(db, uid, password, 'res.partner',
                                'search', [[]], {'limit': 1})

session_data = {
    "name": 'Nikon II',
    "duration": 1,
    "seats": 5,
    "instructor_id": instructor_id,
    "course_id": course_id,
    "attendee_ids": [(6, 0, attendee_id)]
}

id = models.execute_kw(db, uid, password, 'open.academy.session', 'create', [session_data])
