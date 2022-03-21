#!python.exe

import cgi
form = cgi.FieldStorage()

if form.getvalue("final_thesis"):
   final_thesis_flag = "Da"
else:
   final_thesis_flag = "Ne"

print('''
<!DOCTYPE html>
<html>
<head>
    <title>IWA - Vjezba 2</title>
</head>
<body>
<form action="iwa-02_04.py" method="post">
    <table border="1">
        <tr>
            <td>Napomene:</td>
            <td><textarea name="notes" rows="4" cols="20"></textarea></td>
        </tr>
        <tr>
            <td><input type="submit" value="Next"></td>
            <td></td>
        </tr>
    </table>''')

print('<input type="hidden" name="first_name" value="' + form.getvalue("first_name") + '">')
print('<input type="hidden" name="password" value="' + form.getvalue("password") + '">')
print('<input type="hidden" name="repeat_password" value="' + form.getvalue("repeat_password") + '">')
print('<input type="hidden" name="status" value="' + form.getvalue("status") + '">')
print('<input type="hidden" name="email" value="' + form.getvalue("email") + '">')
print('<input type="hidden" name="study_programme" value="' + form.getvalue("study_programme") + '">')
print('<input type="hidden" name="final_thesis" value="' + final_thesis_flag + '">')

print('''</form>
</body>
</html>
''')