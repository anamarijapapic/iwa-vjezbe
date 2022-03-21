#!python.exe

import cgi
import cgitb
cgitb.enable(display=0, logdir="")

print('''
<!DOCTYPE html>
<html>
<head>
    <title>IWA - Vjezba 2</title>
</head>
<body>
<form action="iwa-02_02.py" method="post">
    <table border="1">
        <tr>
            <td>Ime:</td>
            <td><input type="text" name="first_name" required></td>
        </tr>
        <tr>
            <td>Lozinka:</td>
            <td><input type="password" name="password" required></td>
        </tr>
        <tr>
            <td>Ponovi lozinku:</td>
            <td><input type="password" name="repeat_password" required></td>
        </tr>
        <tr>
            <td><input type="submit" value="Next"></td>
            <td></td>
        </tr>
    </table>
</form>
</body>
</html>
''')

form = cgi.FieldStorage()