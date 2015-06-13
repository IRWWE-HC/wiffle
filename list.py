#!/usr/bin/python
print "Content-type: text/html\n"
print ""

x = open("../dir.txt","r")
y = x.readlines()

output = ""

def listsites(x):
    stor = open(x + "/sites/exist.txt","r")
    y = stor.readlines()[1:]
    stor.close()
    output = ""
    for i in y:
        output += "<li>" + i + "</li>"
    return output

for i in y:
    output += "<li class='siteDir'>" + i "'s sites:"
    output += listsites(i)
    output += "</li>

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
	
