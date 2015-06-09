#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb
import os

cgitb.enable()
d=cgi.FieldStorage()
sidebar = ""


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value
# title


# sB-text

sB = {}

def fix():
    pos = 0
    while True:
        key = "sB-text" + str(pos)
        keyd = "sB-link" + str(pos)
        try:
            sB[newDict[key]] = newDict[keyd]
        except:
            break
        pos += 1
                    
fix()


def sidebarify():
    output = ""
    pos = 0
    for i in sB.keys()[::-1]:
        output += "<li> <a href=" + sB[i] + ">" + i + "</a>" + "<br> </li>"
    return output
        
sidebar += sidebarify()
output = ""
if 'm-text' in newDict.keys():
    output += newDict['m-text']

output = output.replace("\n", "<br>")
output = output.replace("\r","")
print output



if "heading" not in newDict.keys():
    newDict["heading"] =  ""

final = ''
final += '''
<!DOCTYPE html>
<html class=
'''
final += newDict["template"] + ">"
final += '''
    <head>
        <link rel="stylesheet" href="css/css-t1.css">
        <title> Website (Fix later) </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/newLink.js"></script>
            <center>
                <span id="heading" class="s1">
'''
final += newDict["heading"]
final += '''
                </span>
            </center>
			
			<div id="sB" class="s1">
			<ul>
'''
final += sidebar
final += '''
			</ul></div>
            <!--Main body of the text. Plain text for now-->
            <div id="m" class="s1">
            '''
final += output
final += '''
			
			</div>
            <br>
            <a href ="../sites"> Sites </a>
    </body>
</html>
'''

f = open("../sites/exist.txt", "r'")
g = f.readlines()
f.close()

last = g[-1]
new = "site" + str((int(last[last.find("e")+1:])) + 1)



f = open("../sites/exist.txt", "a")

if new == "site1":
    f.write("\n")
f.write(new +"\n")
f.close()

os.mkdir("../sites/"+new)
y = open("../sites/"+ new +"/index.html","w")
y.write(final)
y.close()

print final
