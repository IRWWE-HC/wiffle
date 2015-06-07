#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import random
import cgitb

cgitb.enable()
d=cgi.FieldStorage()


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value

if "template" not in newDict.keys():
    newDict[template] = "t" + str(random.randrange(5) + 1)

print '''
<!DOCTYPE html>
<html 
'''
if "template" in newDict.keys():
	print " class="	
	print newDict["template"]
print '''
">
    <head>
        <link rel="stylesheet" href="css/css-t1.css">
        <title> Website Editor </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/newLink.js"></script>
        <form id="form" action="test.py" method="POST">
            
            <input type="hidden" name ="template"  value =
'''
print newDict["template"]
print ">"
print '''
            <center>
                <!--The title input is just the title.-->
                <input type="text" name="heading" id="heading" class="s1"placeholder="Title here">
            </center>
			
			<div id="insertInput">
				<!--Sidebar text. Every new line represents a new sidebar element. Check for those new lines in your python code-->
				<input type="text" name="sB-text0" id="sB-text" class="s1"
										 placeholder="Sidebar Names Here.">

				<!--Sidebar links. Each element of the sidebar should link to something, which is what the links will do. I suggest playing around with parallel lists, and checking if they match up-->
				<input type="text" name="sB-link0" id="sB-link" class="s1"
										 placeholder="Sidebar Links Here.">
				
				<br>
			</div>
            <!--Main body of the text. Plain text for now-->
            <textarea name="m-text" id="m-text" class="s1"
                                    placeholder="Main text here"></textarea>
            <br>

                <input type="submit" value="Submit" id="submit" class="s1">

        </form>
		
    </body>
</html>
'''
