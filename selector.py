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

print '''
<!DOCTYPE html>
<html id=
'''
print newDict["template"]
print '''
"t1">
    <head>
        <link rel="stylesheet" href="css/css-t1.css">
        <title> Website Editor </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/tab.js"></script>
        <form id="form" action="test.py" method="POST">

            <center>
                <!--The title input is just the title.-->
                <input type="text" name="title" id="title" placeholder="Title here">
            </center>
			
			<div id="insertInput">
				<!--Sidebar text. Every new line represents a new sidebar element. Check for those new lines in your python code-->
				<input type="text" name="sB-text0" id="sB-text" class="sB"
										 placeholder="Sidebar Names Here.">

				<!--Sidebar links. Each element of the sidebar should link to something, which is what the links will do. I suggest playing around with parallel lists, and checking if they match up-->
				<input type="text" name="sB-link0" id="sB-link" class="sB"
										 placeholder="Sidebar Links Here.">
				
				<br>
			</div>
            <!--Main body of the text. Plain text for now-->
            <textarea name="m-text" id="m-text"
                                    placeholder="Main text here"></textarea>
            <br>

                <input type="submit" value="Submit" id="submit">

        </form>
		
    </body>
</html>
'''
