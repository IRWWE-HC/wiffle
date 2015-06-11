#!/usr/bin/python
import cgi,cgitb,os,random,hashlib
cgitb.enable()

#----------------General Stuff---------------------

def md5Pass(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt','r').readlines()
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

#----------------Create Profile Functions-----------------
def headerC():
    return """content-type: text/html

<!DOCTYPE HTML>
<html>
<head>
<title>Create account</title>
</head>
<body>
"""

def footerC():
    return """</body>
</html>"""

def valid(s):
    for c in s:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9'):
            return False
    return True

def createAccount(form):
    result = "attempting to create an account...<br>"
    if "user" in form and "pass" in form and "pass2" in form:
        user = form['user'].value
        password = form['pass'].value
        password2 = form['pass2'].value
        if checkIfNameExists(user):
            result += "user exists: "+ user +"<br>"
        elif password != password2:
            result += "passwords do not match!<br>"
        elif not valid(user):
            result += "username contains invalid characters<br>"
        else:
            result += "account "+user+' created! login here: <a href="login.html">login page</a><br>'
            f = open('users.txt','a')
            password = md5Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
            g = open('../users/'+user,'w')
            os.chmod('../users/'+user, 0777)
            os.mkdir('../users/'+user+'/sites')
            os.chmod('../users/'+user+'/sites', 0777)
            h = open('../users/'+user+'/sites/exist.txt',"w")
            os.chmod('../users/'+user+'/sites/exist.txt', 0777)
            h.write("site0")
            g.close()
            h.close()
    else:
        result+="<h1>Invalid form submission, please fill in all fields</h1>"
    return result

def notFilledIn():
    return '''You need to create an account using the form found <a href="create.html">here</a>\n'''

def mainC():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notFilledIn()
    else:
        body += createAccount(form)
    print header() + body + footer()

#----------------Login Functions-----------------

def headerL():
        return """
    <!DOCTYPE HTML>
    <html>
    <head>
    <title>login checker</title>
    </head>
    <body>
    Checking your login status...<br>
    """
    
def footerL():
    return """</body>
</html>"""

def authenticate(user,password):
    password = md5Pass(password+user) # you can make this different, but still unique md5Pass(password+user)
    text = open('users.txt', 'r').readlines()
    for line in text:
        line = line.strip().split(",")
        if line[0]==user:
            if line[1]==password:
                return True
            else:
                return False
    return False

#the following code takes care of making sure the user is recognized
#as being logged in on other parts of the website
#remove a user, only do this if they successfully authenticated
#since this does not check to see if you have the right person
def remove(user):
    infile = open('loggedin.txt','r')
    text = infile.read()
    infile.close()
    if (user+",") in text:
        #remove code
        outfile = open('loggedin.txt','w')
        lines = text.split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].split(",")
            if len(lines[i]) > 1:
                if(lines[i][0] != user):
                    outfile.write(','.join(lines[i])+'\n')
        outfile.close();


#only meant to be run after password authentication passes.
#uses call to remove(user) that will remove them no matter what.
def logInUser(username):
    magicNumber = str(random.randint(1000000,9999999))
    remove(username)
    outfile = open('loggedin.txt','a')
    IP = "1.1.1.1"
    if "REMOTE_ADDR" in os.environ :
        IP = os.environ["REMOTE_ADDR"]
    outfile.write(username+","+magicNumber+","+IP+"\n")
    outfile.close()
    return magicNumber
            
def login(form):
    result = ""
    if not ('user' in form and 'pass' in form):
        return "Username or password not provided"
    user = form['user'].value
    password = form['pass'].value
    if authenticate(user,password):
        result += "Success!<br>\n"
        #add user to logged in status
        magicNumber = logInUser(user)
        result += '<a href="../theme.py?user='+user+'&magicnumber='+str(magicNumber)+'">Click here to go to the main site!</a>'
    else:
        result += "Failed to log in, authentication failure"
    return result


def notLoggedIn():
    return '''You need to login, <a href="login.html">here</a>\n'''

def mainL():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notLoggedIn()
    else:
        body += login(form)
    print header() + body + footer()

#-------------Wrapping it Up--------------

def logCreate():
	query = cgi.FieldStorage()
	if 'passC' in query:
		mainC()
	if 'passL' in query:
		mainL()

logCreate()

