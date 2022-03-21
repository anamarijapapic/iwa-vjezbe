#!python.exe

import cgi
form = cgi.FieldStorage()

first_name = form.getvalue("first_name")

email = form.getvalue("email")

status = form.getvalue("status")

study_programme = form.getvalue("study_programme")

final_thesis = form.getvalue("final_thesis")

if form.getvalue("notes"):
   notes_flag = form.getvalue("notes")
else:
   notes_flag = "Nema napomena"

print('''
<!DOCTYPE html>
<html>
<head>
    <title>IWA - Vjezba 2</title>
</head>
<body>
<form action="" method="post">
    <table border="1">
        <tr>
            <td colspan="2" style="text-align:center;"><b>Uneseni podatci</b></td>
        </tr>
        <tr>
            <td>Ime:</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>E-mail:</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Status:</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Smjer:</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Zavrsni rad:</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Napomene:</td>
            <td>%s</td>
        </tr>
    </table> 
</form>
<a href="iwa-02_01.py">Na pocetak</a>
</body>
</html>
''' % (first_name, email, status, study_programme, final_thesis, notes_flag))