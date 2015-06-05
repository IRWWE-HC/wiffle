#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb

cgitb.enable()
d=cgi.FieldStorage()


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value

output = ""
output += "<!DOCTYPE html>"
output += "<html" + " id=" + newDict["template"] +">"
output +="    <head>"
output +='        <link rel="stylesheet" href="css/css-t1.css">'
output +='        <title> Website Editor </title>'
output +='    </head>'
output +='    <body>'
output +='        <script src="js/jquery-2.1.1.min.js"></script>'		
output +='        <form id="form" action="test.py" method="GET">'
output +='            <center>'
output +='                <!--The title input is just the title.-->'
output +='                <input type="text" name="title" id="title" placeholder="Title here">'
output +='            </center>'
output +='			<div id="insertInput">'
output +='				<!--Sidebar text. Every new line represents a new sidebar element. Check for those new lines in your python code-->'
output +='				<input type="text" name="sB-text" id="sB-text" class="sB"'
output +='										 placeholder="Sidebar Names Here.">'
output +='				<!--Sidebar links. Each element of the sidebar should link to something, which is what the links will do. I suggest playing around with parallel lists, and checking if they match up-->'
output +='				<input type="text" name="sB-link" id="sB-link" class="sB"'
output +='										 placeholder="Sidebar Links Here.">'	
output +='				<br>'
output +='			</div>'
output +='            <!--Main body of the text. Plain text for now-->'
output +='            <textarea name="m-text" id="m-text"'
output +='                                    placeholder="Main text here"></textarea>'
output +='            <br>'
output +='            <center>'
output +='                <input type="submit" value="Submit" id="submit">'
output +='            </center>'
output +='        </form>'		
output +='    </body>'	
output +='	<script src="js/tab.js"></script>'
output +='</html>'

print output

