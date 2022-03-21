#!python.exe

import cgi
form = cgi.FieldStorage()

password = form.getvalue("password")
repeat_password = form.getvalue("repeat_password")
# passwords must match
if (password != repeat_password):
    print("Location: iwa-02_01.py")

print('''
<!DOCTYPE html>
<html>
<head>
    <title>IWA - Vjezba 2</title>
</head>
<body>
<form action="iwa-02_03.py" method="post">
    <table border="1">
        <tr>
            <td>Status:</td>
            <td>
                Redovan: <input type="radio" name="status" value="Redovan" checked>
                Izvanredan: <input type="radio" name="status" value="Izvanredan">
            </td>
        </tr>
        <tr>
            <td>E-mail:</td>
            <td><input type="email" name="email" required></td>
        </tr>
        <tr>
            <td>Smjer:</td>
            <td>
                <select name="study_programme">
                    <option value="Baze podataka" selected>Baze podataka</option>
                    <option value="Programiranje">Programiranje</option>
                    <option value="Racunalne mreze">Racunalne mreze</option>
                    <option value="Informacijski sustavi">Informacijski sustavi</option>
                </select>
            </td>
        </tr>
        <tr>
            <td>Zavrsni:</td>
            <td><input type="checkbox" name="final_thesis" value="Da"></td>
        </tr>
        <tr>
            <td><input type="submit" value="Next"></td>
            <td></td>
        </tr>
    </table>''')

print('<input type="hidden" name="first_name" value="' + form.getvalue("first_name") + '">')
print('<input type="hidden" name="password" value="' + form.getvalue("password") + '">')
print('<input type="hidden" name="repeat_password" value="' + form.getvalue("repeat_password") + '">')

print('''</form>
</body>
</html>
''')