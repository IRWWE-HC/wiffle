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
    pos = 0
    while pos != len(y):
	y[pos] = y[pos].split(";")
	pos += 1
    output = '<ul class="siteDir">'
    #print y
    #for i in y:
	#if i[1] == "<table>":
	 #   i[1] = ""
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
		<link href="favicon.ico" rel="icon" type="image/x-icon" />
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
