#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import random
import cgi,cgitb,os

cgitb.enable()

#the field storage is a global variable.
#Since your page has exactly one, you can
#just acccess it from anywhere in the program.
form = cgi.FieldStorage()

def header(user,magicnumber):
        final += """
    <!DOCTYPE HTML>
    <html>
    <head>
    <link rel="stylesheet" href="css/template.css">
        <title> Theme Selector </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/master.js"></script>
		  <nav class="navBar">
			<a href="login/homepage.html" id="home"> IRWWE-HC </a>
			<ul class="navBarRight">
				<li> <a href="list.py"> Sites Directory
				</a> </li>
				<li> <a href="about.html"> About Us </a> </li>
				<li> <a href="login/logout.py?"""
        final += "user=" + user +"&magicnumber=" + magicnumber
        final += """
        "> Sign Out
				</a> </li>
			</ul>
		</nav>
    """
        return final


def footer():
    return """</body>
</html>"""



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
    return html

def notLoggedIn():
    return '''You need to login to see more. You can log in here: <a href="login/homepage.html">here</a>\n'''

html = '''		<h1 class="USdirHeading"> Please Choose Your Theme </h1>
		<h2 class="templateChoice"> Choose a template! </h1>
		<form 
			name = "input"
			method = "GET"
			action = "selector.py"
		>
			<input type="radio" name="template" value = "t1" id="t1" class="templateRadio" checked> 
			<label for="t1">Template 1</label> <br>
			
			<input type="radio" name="template" value = "t2" id="t2" class="templateRadio"> 
			<label for="t2">Template 2</label> <br>
			
			<input type="radio" name="template" value = "t3" id="t3" class="templateRadio">  
			<label for="t3">Template 3</label> <br>
			
			<input type="radio" name="template" value = "t4" id="t4" class="templateRadio"> 
			<label for="t4">Template 4</label> <br>
			
			<input type="radio" name="template" value = "t5" id="t5" class="templateRadio"> 
			<label for="t5">Template 5</label> <br>
			
            <input type="hidden" name="user" value='''
html += "'"+form['user'].value+"'>"
html += '<input type="hidden" name="magicnumber" value='
html += "'"+form['magicnumber'].value+"'>"
html += '''\
			<input type="submit" value="To Next Process" id="submitButton"> <br>
			
			<img id="img1" class="templateIMG" src="templates/template1.png">
			<img id="img2" class="templateIMG" src="templates/template2.png">
			<img id="img3" class="templateIMG" src="templates/template3.png">
			<img id="img4" class="templateIMG" src="templates/template4.png">
			<img id="img5" class="templateIMG" src="templates/template5.png">
		</form>
'''

def main():
    body = ""

    isLoggedIn = authenticate()

    #use this to determine if you want to show "logged in " stuff, or regular stuff
    if isLoggedIn:
        body += loggedIn()
    else:
        body += notLoggedIn()
        print header("","") +body + footer()
    #attach a logout link only if logged in
    if isLoggedIn:
        body+= makeLink("login/logout.py","Click here to log out")+"<br>"
        print header(form['user'].value, form['magicnumber'].value) + body + footer()

main()
