#!python.exe

import cgi
import base
import subjects

params = cgi.FieldStorage()

year = params.getvalue('year')

status = dict.fromkeys(subjects.subjects)
for key in subjects.subjects:
    status[key] = subjects.choose_status(key, params.getvalue(key))

# print subject with info and radio buttons
def print_subject(subjects_key):
    print('''
    <tr>
        <td>''' + subjects.subjects[subjects_key]['name'] + '''</td>
        <td>''' + str(subjects.subjects[subjects_key]['ects']) + '''</td>
        <td>
    ''')
    for status_key, status_value in subjects.status_names.items():
        print(status_value + '<input type="radio" name="' + subjects_key + '" value="' + status_value + '"' + subjects.manage_radio_check(subjects_key, status, status_value))
    print('''
        </td>
    </tr>
    ''')

# print all subjects of the chosen year of study
def print_subjects_year(currYear):
    print('''
    <table border="1">
        <tr>
            <td colspan="3">''' + currYear + '''</td>
        </tr>
        <tr>
            <td>Subject</td>
            <td>Ects</td>
            <td>Status</td>
        </tr>
    ''')
    for year_key, year_value in subjects.year_names.items():    
        for subjects_key, subjects_value in subjects.subjects.items():
            if subjects_value['year'] == year_key and year_value == currYear:
                print_subject(subjects_key)
    print('</table>')

# print enrollment list - all subjects from all years, their statuses and calculate ects
def print_enrollment_list():
    total_ects = 0

    print('''
    <table border="1">
        <tr>
            <td>Subject</td>
            <td>Status</td>
            <td>Ects</td>
        </tr>
    ''')

    for subjects_key, subjects_value in subjects.subjects.items():
        if subjects.check_status(subjects_key, status) == subjects.status_names['pass']:
            total_ects += subjects.subjects[subjects_key]['ects']
            
        print('''
        <tr>
            <td>''' + subjects.subjects[subjects_key]['name'] + '''</td>
            <td>''' + subjects.check_status(subjects_key, status) + '''</td>
            <td>''' + str(subjects.subjects[subjects_key]['ects']) + '''</td>
        </tr>''')        

    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(total_ects) + '''</td>
    </tr>''')
    print('</table>')

base.start_html_form()
subjects.display_buttons()
if params.getvalue('enrollment_list') != None:
    print_enrollment_list()
else:
    print_subjects_year(params.getvalue('year'))
base.end_html_form()