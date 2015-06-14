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
		You must login to submit. You can login <a href="login/homepage.html"> here </a>.
    </body>
</html>
'''

def checkLogCarousel():
    #determine if the user is properly logged in once. 
    isLoggedIn = authenticate()
    optionCarousel = ""

    #use this to determine if you want to show "logged in " stuff, or regular stuff
    if isLoggedIn:
        optionCarousel += endstring
    else:
        optionCarousel += notLoggedIn()
    #attach a logout link only if logged in
    return optionCarousel

def checkLogSignOut():
    isLoggedIn = authenticate()
    logOutLink = ""
    if isLoggedIn:
        logOutLink+= makeLink("login/logout.py","Sign Out")
    else:
        logOutLink+= '<a href="login/homepage.html"> Sign In </a>'
    return logOutLink

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
			<a href="login/homepage.html" id="home"> Wiffle </a>
			<ul class="navBarRight">
				<li> <a href="list.py"> Sites Directory
				</a> </li>
				<li> <a href="about.html"> About Us </a> </li>
				<li>
'''
final += checkLogSignOut()
final += '''
				 </li>
			</ul>
		</nav>
        <form id="form" action="output.py" method="POST">
			<div id="titleContainer">
				<h1 id="titleInstruc"> Please Name Your Website </h1>
				<input type="text" name="title" id="title" class="s1" placeholder="Website Name Here">
				<button type="button" value="finish" id="finish"> Done! </button>
				<h2 id="otherInstruc"> Hover over the + Button to Begin </h2>
			</div>
            <input type="hidden" name ="template"  value =
'''
final += newDict["template"]
final += ">"
final += "<input type='hidden' name ='user' value ="
final += newDict['user']
final += ">"
final += '''
				<h1 id="headingDisplay" class="s1"> Title Here </h1>
				<div id="headingDIV" class="s1">
					<div id="outsideHeading" class="outside"></div>
					<input type="text" name="heading" id="heading" class="s1" placeholder="Title here">
				</div>

			
			<div id="insertSB">
				<h1 id="sB-nameDisplay"> Sidebar Name Here </h1><!--
				--><button type="button" value="addSidebarInstruction" id="addSidebarInstruction" class="s1"> + </button>
					<div id="sB-name">
						<div class="outside"></div>
						<input type="text" name="sB-name" placeholder="Put name here">
					</div>
				<br>
				<br>
				<div id="sBInput">
				
					<div id="sBInputInstruction">
						<h1 id="instruction0"> Click to Add New Sidebar Link </h1>
					</div>
					
					<div id="val0" class="sBInputVal">
						<div id= "sBInputOutside" class="outside"></div>
						<input type="text" name="sB-text0" id="sB-text" class="s1" placeholder="Text">
						<input type="text" name="sB-link0" id="sB-link" class="s1" placeholder="Link">
					</div>

					<span id="alert"> Friendly Reminder: Fill Out Both Fields! </span>
					
				</div>
				<br>
			</div>
            <!--Main body of the text. Plain text for now-->
			
			<div id="m-textOutput" class="s1"><p id="removePlease">Click to load editor</p></div>
			
			<div id="m-text">
				<div id="m-textOutside" class="outside"></div>
			
				<textarea name="m-text" id="m-textInput" class="s1"
                                    placeholder="Main text here"></textarea>
			</div>
            <br>
'''
endstring = '''
			<div id="optionCarousel">
				<button type="button" value="optionList" id="optionList"> + </button>
				
                <input type="submit" value="Submit" id="submit" class="optionButton">

				<button type="button" value="optionTitle" id="optionTitleAdd" class="optionButton"> Title </button>
				
				<button type="button" value="optionMT" id="optionMTAdd" class="optionButton"> Main Text </button>
				
				<button type="button" value="optionSB" id="optionSBAdd"  class="optionButton"> Sidebar </button>
			</div>
				
        </form>
		
    </body>
</html>

'''

    
def main():
    body = ""
    #use this to add stuff to the page that anyone can see.
    body += final
    body += checkLogCarousel()
    print body


main()
