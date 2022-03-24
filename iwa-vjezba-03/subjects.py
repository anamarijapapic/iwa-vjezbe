#!python.exe

from http import cookies
import os

subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    };
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    };

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
};

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
};

def display_buttons():
    print('<div>')
    for key in year_ids:
        print('<input type="submit" name="year" value="' + key + '"/>')
    print('<input type="submit" name="enrollment_list" value="Enrollment List"/>')
    print('</div>')

# save chosen status to cookies
def choose_status(subject_id, status=None):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    if status is not None:
        cookie = cookies.SimpleCookie()
        cookie[subject_id] = status
        print(cookie.output())
    elif all_cookies_object.get(subject_id):
        status = all_cookies_object.get(subject_id).value
    else:
        status = status_names['not']
    return status

def check_status(subject_id, status):
    return status[subject_id]

def manage_radio_check(subject_id, status, status_value):
    if check_status(subject_id, status) == status_value:
        return ' checked/>'
    return '/>'