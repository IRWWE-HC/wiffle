#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb

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

'''
print stor1
print "<br>"
print stor2
print "<br>"
#print d
print "<br>"
print newDict
print "<br>"
print newDict["title"]
def fixstor(x):
    temp = x
    if temp.find("\r") != -1:
        temp = temp.replace("\r", "")
    temp = temp.split("\n")
    return temp

stor3 = fixstor(stor1)
stor4 = fixstor(stor2)
'''

#print stor3
#print stor4

def sidebarify():
    output = ""
    pos = 0
    for i in sB.keys():
        output += "<li> <a href=" + sB[i] + ">" + i + "</a>" + "<br> </li>"
    return output
        
sidebar += sidebarify()
output = ""
if 'm-text' in newDict.keys():
    output += newDict['m-text']

output.replace("\n", "<br>")
output.replace("\r","")



if "title" not in newDict.keys():
    newDict["title"] =  ""















print '''
<!DOCTYPE html>
<html class=
'''
print newDict["template"] + ">"
print '''
    <head>
        <link rel="stylesheet" href="css/css-t1.css">
        <title> Website (Fix later) </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/tab.js"></script>
            <center>
                <span id="title" class="s1"> Text Here </span>
            </center>
			
			<div id="sB" class="s1">
			<ul>
'''
print sidebar
print '''
			</ul></div>
            <!--Main body of the text. Plain text for now-->
            <div id="m" class="s1">
            '''
print output
print '''
			
			</div>
            <br>		
    </body>
</html>
'''
