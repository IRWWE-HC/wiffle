#!/usr/bin/python
import random
import cgi,cgitb,os

cgitb.enable()

#the field storage is a global variable.
#Since your page has exactly one, you can
#just acccess it from anywhere in the program.
form = cgi.FieldStorage()

def header():
        return """content-type: text/html

    <!DOCTYPE HTML>
    <html>
    <head>
    <title>page of my website...</title>
    </head>
    <body>
    """


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
    return '''You need to login to see more. You can log in here: <a href="login/login.html">here</a>\n'''

html = '''		<h1> Welcome to IRWWE-HC's Final Project! </h1>
		<h2> Choose a template! </h1>
		<form 
			name = "input"
			method = "POST"
			action = "selector.py"
		>
			<input type="radio" name="template" value = "t1"> Template 1 
			<input type="radio" name="template" value = "t2"> Template 2
			<input type="radio" name="template" value = "t3"> Template 3 
			<input type="radio" name="template" value = "t4"> Template 4 
			<input type="radio" name="template" value = "t5"> Template 5
                        <input type="hidden" name="user" value='''
html += "'"+form['user'].value+"'>"
html += '<input type="hidden" name="magicnumber" value="'
html += "'"+form['magicnumber'].value+"'>"
html += '''
			<input type="submit" value="To Next Process">
		</form>
'''

def main():
    body = ""
    #use this to add stuff to the page that anyone can see.


    #determine if the user is properly logged in once. 
    isLoggedIn = authenticate()

    #use this to determine if you want to show "logged in " stuff, or regular stuff
    if isLoggedIn:
        body += loggedIn()
    else:
        body += notLoggedIn()

    #anyone can see this
    body += "<hr>other stuff can go here<hr>\n"
    
    #attach a logout link only if logged in
    if isLoggedIn:
        body+= makeLink("login/logout.py","Click here to log out")+"<br>"

    #make links that include logged in status when the user is logged in
    #finally print the entire page.
    print header() + body + footer()

main()
 
