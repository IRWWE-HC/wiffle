#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb
import os

cgitb.enable()
d=cgi.FieldStorage()
sidebar = ""


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value

if 'user' in newDict.keys():
    key = newDict['user']
# title


# sB-text

sBt = []
sBl = []

def fix():
    pos = 0
    while True:
        key = "sB-text" + str(pos)
        keyd = "sB-link" + str(pos)
        try:
            sBt += newDict[key]
	    sBl += newDict[keyd]
        except:
            break
        pos += 1
                    
fix()
print sBt
print sBl
'''
stor1 = sB.keys()
stor2 = sB.keys()[::-1]

print stor1,stor2
for i in stor1:
    print i
print "====="

for i in stor2:
    print i
'''   
def sidebarify():
    output = ""
    pos = 0
    while pos != len(sBt):
        output += "<pre> <li> <a href='" + sBl[pos] + "'>" +  sBt[pos] + "</a>" + "<br> </li></pre>"
    	pos += 1
    return output
        
sidebar += sidebarify()
output = ""
if 'm-text' in newDict.keys():
    output += newDict['m-text']

output = output.replace("\n", "<br>")
output = output.replace("\r","")



if "heading" not in newDict.keys():
    newDict["heading"] =  ""

final = ''
final += '''
<!DOCTYPE html>
<html class=
'''
final += newDict["template"] + ">"
final += '''
    <head>
        <link rel="stylesheet" href="../../../../css/css-t1.css">
        <title> Website (Fix later) </title>
    </head>
    <body>
        <script src="../../../../js/jquery-2.1.1.min.js"></script>
		<script src="../../../../js/newLink.js"></script>
                <nav class="navBar">
			<a href="../../../../selector.py" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>
                <span id="heading" class="s1">
'''
final += newDict["heading"]
final += '''
                </span>
			
			<div id="insertSB" class="s1">
			<ul id="sB" class="s1">
'''
final += sidebar
final += '''
			</ul></div>
            <!--Main body of the text. Plain text for now-->
            <div id="m-textOutput" class="s1">
            '''
final +="<pre>" +  output + "</pre>"
final += '''
			
			</div>
            <br>
    </body>
</html>
'''

final2 = ''
final2 += '''
<!DOCTYPE html>
<html class=
'''
final2 += newDict["template"] + ">"
final2 += '''
    <head>
        <link rel="stylesheet" href="css/css-t1.css">
        <title> Website (Fix later) </title>
    </head>
    <body>
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js/newLink.js"></script>
		<nav class="navBar">
			<a href="selector.py" id="home"> Website Editor </a>
			<ul class="navBarRight">
				<li> <a href="http://bart.stuy.edu/~richard.lin"> Richard </a> </li>
				<li> <a href="http://bart.stuy.edu/~edward.tsang"> Edward </a> </li>
			</ul>
		</nav>
                <span id="heading" class="s1">
'''
final2 += newDict["heading"]
final2 += '''
                </span>
            </center>
			
			<div id="insertSB" class="s1">
			<ul id="sB" class="s1">
'''
final2 += sidebar
final2 += '''
			</ul></div>
            <!--Main body of the text. Plain text for now-->
            <div id="m-textOutput" class="s1">
            '''
final2 += output
final2 += '''
			
			</div>
            <br>
            Sites created by: <a href ='users/
'''
final2 += key + "/sites"
final2 += "'>" + key + "</a>"
final2 +='''
    </body>
</html>
'''


\

'''
userDict = open("login/users.txt","r")
r = userDict.readlines()
pos = 0
rp
while pos != len(r):
    rp += r[pos].split(",")
    pos += 1

listUsers = []
for i in rp:
    listUsers += i[0]
'''
'''
listUsers = open("dir.txt", "r")
print listUsers
userl = listUsers.readlines()
print userl
listUsers.close()

print userl

if key not in userl:
    xl = open("dir.txt","a")
    xl.write(key + "\n")
    xl.close()
    os.mkdir('users/'+key)
    os.chmod('users/'+key, 0777)
    os.mkdir('users/'+key+'/sites')
    os.chmod('users/'+key+'/sites', 0777)
    p = open('users/'+key+'/sites/exist.txt',"w")
    os.chmod('users/'+key+'/sites/exist.txt', 0777)
    p.write("site0")
    p.close()
'''

tyruf = open("users/" + key + "/sites/exist.txt", "r'")
tyrug = tyruf.readlines()
tyruf.close()

last = tyrug[-1]
print last
new = "site" + str((int(last[(last.find("e")+1):])) + 1)
    

f = open("users/"+ key +"/sites/exist.txt", "a")

if new == "site1":
    f.write("\n")
f.write(new +"\n")
f.close()

os.mkdir("users/"+ key +"/sites/"+new)
y = open("users/"+ key + "/sites/"+ new +"/index.html","w")
y.write(final)
os.chmod("users/"+ key + "/sites/"+ new, 0777)
y.close()

k = open("users/" + key + "/sites/"+new+"/users.txt","w")
k.write(key +"\n")
k.close()

print final2
