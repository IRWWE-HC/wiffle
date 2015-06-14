#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi

final = ""

x = open("dir.txt","r")
f = x.read()
f = f.split("\n")

d = cgi.FieldStorage()

if 'user' in d:
    key = d['user'].value
else:
    key = ""


def listsites(x):
    output = ""
    if key not in f and key != "" or 'user' not in d:
        output += "User not found"
	return output
    else:
        stor = open("users/" + x + "/sites/exist.txt","r")
        y = stor.readlines()[1:]
        stor.close()
	pos = 0
        while pos != len(y):
            y[pos] = y[pos].split(';')
	    pos += 1
        output += "<ul class='uS'>"
        for i in y:
            output += "<li> <a href='users/" + x + "/sites/" + i[0] + "'>"  + i[1] + "</a> </li>"
        return output + "</ul>"




final += '''
<!DOCTYPE html>
	<html>
		<head>
			<title>
'''
final += key + "'s sites"
final += '''</title>
<link rel="stylesheet" href="css/template.css">
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/master.js"></script>
		  <nav class="navBar">
			<a href="login/homepage.html" id="home"> Wiffle </a>
			<ul class="navBarRight">
				<li> <a href="list.py"> Sites Directory
				</a> </li>
				<li> <a href="about.html"> About Us </a> </li>
				</a> </li>
			</ul>
		</nav>

		<body>
'''
final +='		<h1 class="USdirHeading">'
final += key + "'s Sites </h1>"
final += listsites(key)
final += '''

		</body>

	</html>
'''
	
print final
