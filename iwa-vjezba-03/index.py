#!python.exe

import cgi
import os
from http import cookies
import base
import subjects

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()

subjects.set_cookies(params)
dictionary = subjects.get_cookies(all_cookies_object)

base.start_html_form()
subjects.display_buttons()
if params.getvalue('button') == 'Enrollment List':
    subjects.print_enrollment_list(dictionary, params)
elif params.getvalue('button') != None:
    subjects.print_subjects_year(params.getvalue('button'), dictionary)
base.end_html_form()