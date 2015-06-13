#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import random
import cgitb
import os

cgitb.enable()
d=cgi.FieldStorage()


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value

if "template" not in newDict.keys():
    newDict['template'] = "t" + str(random.randrange(5) + 1)





form = cgi.FieldStorage()


def authenticate():
    if 'user' in form and 'magicnumber' in form:
        #get the data from form, and IP from user.
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        IP = 'NULL'
        if 'REMOTE_ADDR' in os.environ:
            IP = os.environ["REMOTE_ADDR"]
        #compare with file
        text = open('login/loggedin.txt').readlines()
        for line in text:
            line = line.strip().split(",")
            if line[0]==user:#when you find the right user name
                if line[1]==magicnumber and line[2]==IP:
                    return True
                else:
                    return False
        return False#in case user not found
    return False #no/missing fields passed into field storage


#either returns ?user=__&magicnumber=__  or an empty string.
def securefields():
    if 'user' in form and 'magicnumber' in form:
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        return "?user="+user+"&magicnumber="+magicnumber
    return ""

#makes a link, link will include secure features if the user is logged in
def makeLink(page, text):
    return '<a href="'+page+securefields()+'">'+text+'</a><br>'

def loggedIn():
    return '''
This part is super secret!<br>
My secret? I hate fleas... even at flea markets.<br>
'''

def notLoggedIn():
    return '''  </form>
		You must login to submit. You can login <a href="login/login.py"> here </a>.
    </body>
</html>
'''

if 'user' not in newDict.keys():
    newDict['user']=""
final = '''
<!DOCTYPE html>
<html 
'''
if "template" in newDict.keys():
	final += " class="	
	final += newDict["template"]
final += '''
">
    <head>
        <link rel="stylesheet" href="css/template.css">
        <title> Website Editor </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>
        <form id="form" action="output.py" method="POST">
            
            <input type="hidden" name ="template"  value =
'''
final += newDict["template"]
final += ">"
final += "<input type='hidden' name ='user' value ="
final += newDict['user']
final += ">"
final += '''
             <center id="titleCenter">
                <!--The title input is just the title.-->
                <input type="text" name="heading" id="heading" class="s1" placeholder="Title here">
            </center>
			
			<div id="insertSB">
				<!--Sidebar text. Every new line represents a new sidebar element. Check for those new lines in your python code-->
				<input type="text" name="sB-text0" id="sB-text" class="s1" placeholder="Text"><!--
				Sidebar links. Each element of the sidebar should link to something, which is what the links will do. I suggest playing around with parallel lists, and checking if they match up. Also this comment serves as a way to make the input be on one line. By doing so, I can get rid of a pesky space between the two inputs
				--><input type="text" name="sB-link0" id="sB-link" class="s1" placeholder="Link. <alt> to add line.">
				<br>
			</div>
            <!--Main body of the text. Plain text for now-->
            <textarea name="m-text" id="m-textInput" class="s1"
                                    placeholder="Main text here"></textarea>
            <br>
'''
endstring = '''
                <input type="submit" value="Submit" id="submit" class="s1">

        </form>
		
    </body>
</html>
'''

def main():
    body = ""
    #use this to add stuff to the page that anyone can see.
    body += final

    #determine if the user is properly logged in once. 
    isLoggedIn = authenticate()

    #use this to determine if you want to show "logged in " stuff, or regular stuff
    if isLoggedIn:
        body += endstring
    else:
        body += notLoggedIn()
    #attach a logout link only if logged in

    if isLoggedIn:
        body+= makeLink("login/logout.py","Click here to log out")+"<br>"

    print body

main()
