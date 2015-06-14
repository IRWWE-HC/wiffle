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
    output = "<ol>"
    for i in y:
        output += "<li> <a href='users/" + x + "/sites/" + i + "'>"  + i + "</a> </li>"
    return output + "</ol>"

for i in y[:-1]:
    output += "<li class='siteDir'>" + i + "'" + "s sites:"
    output += listsites(i)
    output += "</li>"

final = '''
<!DOCTYPE html>
	<html>
		<head>
			<title> Users </title>
<link rel="stylesheet" href="css/template.css">
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/master.js"></script>
		  <nav class="navBar">
			<a href="login/homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>

		<body>
		<h1> Users Sites and Stuff </h1>
			<ul class="userDir">
'''
final += output
final += '''
			</ul>
			
		</body>

	</html>
'''
	
print final
