#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi,cgitb,os,random,hashlib
cgitb.enable()

query = cgi.FieldStorage()
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
def headerC(x):
    if x == 0: #If it fails
        return """ <!DOCTYPE HTML>
                    <html>
                    <head>
                    <title>Create account</title>
                    <meta http-equiv="refresh" content = "2;URL='http://bart.stuy.edu/~edward.tsang/wiffle/login/homepage.html'"/>
                    <link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>
                """
    if x == 1: # If it works
        final = ""
        final += """ <!DOCTYPE HTML>
<html>
<head>
<title>Create account</title>
"""
        final += '<meta http-equiv="refresh" content = "2;URL='
        final += "'http://bart.stuy.edu/~edward.tsang/wiffle/login/homepage.html'"
	final += """ " """
        final += "/>"
        final += """
                    <link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>
"""
        return final

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
    if "user" in form and "passC" in form and "passC2" in form:
        user = form['user'].value
        password = form['passC'].value
        password2 = form['passC2'].value
        if checkIfNameExists(user):
            result += "User Exists: "+ user + ". You will be redirected momentarily. "+"<br>"
        elif password != password2:
            result += "Passwords do not match!" + " You will be redirected momentarily." + "<br>" 
        elif not valid(user):
            result += "Username contains invalid characters." + " You will be redirected momentarily." + "<br>"
        else:
            result += "account "+user+' created! login here if you are not automatically redirected: <a href="homepage.html">login page</a><br>'
            f = open('users.txt','a')
            password = md5Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
            os.mkdir('../users/'+user)
            os.chmod('../users/'+user, 0777)
            os.mkdir('../users/'+user+'/sites')
            os.chmod('../users/'+user+'/sites', 0777)
            p = open('../users/'+user+'/sites/exist.txt',"w")
            os.chmod('../users/'+user+'/sites/exist.txt', 0777)
            p.write("site0")
            p.close()
            x = open("../dir.txt", "a")
            x.write(user + "\n")
            x.close()
    #elif "passC" == "passC2":
	#result+="<h1> Invalid form submission, please fill in all fields</h1>"
    else:
        result+="<h1>Invalid form submission, please fill in all fields</h1>"
    return result

def notFilledIn():
    return '''You need to create an account using the form found <a href="homepage.html">here</a>\n'''

def mainC():
    body = ""
    if len(query)==0:
        body += notFilledIn()
        #print "I don't work"
	#print "<br>"
	#print query
	return headerC(0) + body + footerC()
    else:
        body += createAccount(query)
        #print "I work"
	#print "<br>"
	#print query
	return headerC(1) + body + footerC()

#----------------Login Functions-----------------

def headerL(x,user,magicNumber):
    if x == 0: #If it fails
        return """ <!DOCTYPE HTML>
    <html>
    <head>
    <title>Login Checker</title>
    <META http-equiv="refresh" content = "2;URL='http://bart.stuy.edu/~edward.tsang/wiffle/login/homepage.html'"/>
                    <link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
			</nav>
    Checking your login status...<br>
    """
    if x == 1: # If it works
        final = ""
        final += """ <!DOCTYPE HTML>
<html>
<head>
<title>Login Checker</title>
"""
        final += '<META http-equiv="refresh" content = "0;URL='
        final += 'http://bart.stuy.edu/~edward.tsang/wiffle/theme.py?user='+user+'&magicnumber='+str(magicNumber)+'"/>' 
        final += """
                    <link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
			</nav>
Checking your login status...<br>
"""
        return final
    
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
mag = []
def logInUser(username):
    magicNumber = str(random.randint(1000000,9999999))
    remove(username)
    outfile = open('loggedin.txt','a')
    IP = "1.1.1.1"
    if "REMOTE_ADDR" in os.environ :
        IP = os.environ["REMOTE_ADDR"]
    outfile.write(username+","+magicNumber+","+IP+"\n")
    outfile.close()
    mag.append(magicNumber)
    return magicNumber

            
def login(form):
    result = ""
    if not ('user' in form and 'passL' in form):
        return "Username or password not provided"
    user = form['user'].value
    password = form['passL'].value
    if authenticate(user,password):
        result += "Success!<br>\n"
        #add user to logged in status
        magicNumber = logInUser(user)
        result += '<a href="../theme.py?user='+user+'&magicnumber='+str(magicNumber)+'">If you are not automatically redirected, click here to go to the theme selector!</a>'
    else:
        result += "Failed to log in, authentication failure." + " You will be redirected momentarily."
    return result


def notLoggedIn():
    return '''You need to login, <a href="homepage.html">here</a>\n'''

def mainL():
    body = ""
    if len(query)==0:
        body += notLoggedIn()
        return headerL(0,query['user'].value,mag[0]) + body +footerL()
    else:
        body += login(query)
        return headerL(1,query['user'].value,mag[0]) + body + footerL()

#-------------Wrapping it Up--------------

broken = """
<!DOCTYPE html>
<html>
    <head>
    <meta http-equiv="refresh" content = "2;URL='homepage.html'"/>
        <title> Oh no! </title>
                    <link rel="stylesheet" href="../css/template.css">
    </head>
    <body>
        <script src="../js/jquery-2.1.1.min.js"></script>
		<script src="../js/master.js"></script>
		  <nav class="navBar">
			<a href="homepage.html" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
        You left fields blank! Go back <a href="homepage.html"> here </a> to fix it.
    </body>
</html>        
"""
def logCreate():
    if 'passC' in query:
	   return mainC()
    elif 'passL' in query:
	   return mainL()
    else:
	   return broken


print logCreate()

