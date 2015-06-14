#!/usr/bin/python
print "Content-type: text/html\n"
print ""

x = open("dir.txt","r")
y = x.read()
y = y.split("\n")

output = ""

def listsites(x):
    stor = open("users/" + x + "/sites/exist.txt","r")
    y = stor.readlines()[1:]
    stor.close()
    for i in y:
        i.split(";")
    output = '<ul class="siteDir">'
    for i in y:
        output += "<li> <a href='users/" + x + "/sites/" + i[0] + "'>"  + i[1] + "</a> </li>"
    return output + "</ul>"

for i in y[:-1]:
    output += "<li>" + i
    output += listsites(i)
    output += "</li>"

final = '''
<!DOCTYPE html>
	<html>
		<head>
			<title> Users and Sites Directory </title>
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
		<h1 class="USdirHeading"> Users and Sites Directory </h1>
			<ul class="userDir">
'''
final += output
final += '''
			</ul>
			
		</body>

	</html>
'''
	
print final
