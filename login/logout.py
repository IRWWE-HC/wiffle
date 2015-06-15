#!/usr/bin/python
import cgi,cgitb,os
#cgitb.enable()
def header():
    return """content-type: text/html

<!DOCTYPE HTML>
<html>
<head>
<link href="../favicon.ico" rel="icon" type="image/x-icon" />
<title>Logout</title>
<link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Wiffle </a>
			<ul class="navBarRight">
				<li> <a href="../list.py"> Sites Directory
				</a> </li>
				<li> <a href="../about.html"> About Us </a> </li>
				</a> </li>
			</ul>
		</nav>

Attempting to log you out...<br>

"""

def footer():
    return """</body>
</html>"""

#remove a user, only do this if they successfully authenticated
#since this does not check to see if you have the right person
def remove(user,magicnumber):
    text = open('loggedin.txt','r').read()
    result = "User not logged out<br>\n"
    if (user+",") in text:
        #remove code
        outfile = open('loggedin.txt','w')
        lines = text.split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].split(",")
            if len(lines[i]) > 2:
                if(lines[i][0] != user or lines[i][1] != str(magicnumber) ):
                    outfile.write(','.join(lines[i])+"\n")
                else:
                    result = "Logged out user<br>\n"
        outfile.close();
    else:
        result = "User not found<br>\n"
    return result


def processForm(form):
    if( 'user' in form and 'magicnumber' in form):
        user = form.getvalue('user')
        mn = form.getvalue('magicnumber')
        return remove(user,mn)
    return "You must be logged in properly to log out!<br>\n"

def notLoggedIn():
    return "You must be loggedin before trying to log out!<br>\n"

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notLoggedIn()
    else:
        body += processForm(form)
    print header() + body + footer()

main()
