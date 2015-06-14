#!/usr/bin/python
print "Content-type: text/html\n"
print ""

x = open("dir.txt","r")
y = x.read()
y = y.split("\n")

output = ""

def listsites(x):
    stor = open(x + "users/sites/exist.txt","r")
    y = stor.readlines()[1:]
    stor.close()
    output = "<ol>"
    for i in y:
        output += "<li> <a href='users" + x + "/sites/" + i + "'>"  + i + "</a> </li>"
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
		</head>
		
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
