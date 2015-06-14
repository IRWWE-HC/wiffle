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




sBt = []
sBl = []
'''
textMax = ""
linkMax = ""
while textMax in newDict.keys():
	textpos = 0
	textMax  = "sB-text" + str(pos)
	textpos += 1
	print textMax
while linkMax in newDict.keys():
	linkpos = 0
	linkMax = "sB-link" + str(pos)
	linkpos += 1
	print linkMax

print textMax
print linkMax
'''
def fix():
    pos = 0
    while True:
        key = "sB-text" + str(pos)
        keyd = "sB-link" + str(pos)
        try:
            sBt.append(newDict[key])
	    sBl.append(newDict[keyd])
        except:
            break
        pos += 1

                    
fix()
#print sBt
#print sBl
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
        output += "<a href='" + sBl[pos] + "'>" +  sBt[pos] + "</a><br>"
    	pos += 1
    return output
        
sidebar += sidebarify()
output = ""
if 'm-text' in newDict.keys():
    output += newDict['m-text']

output = output.replace("\n", "<br>")
output = output.replace("&nbsp"," ")
output = output.replace("\r","")



if "heading" not in newDict.keys():
    newDict["heading"] =  ""
if "sB-name" not in newDict.keys():
    newDict["sB-name"] = ""
if "title" not in newDict.keys():
    newDict["title"] = ""

final = ''
final += '''
<!DOCTYPE html>
<html class=
'''
final += newDict["template"] + ">"
final += '''
    <head>
        <link rel="stylesheet" href="../../../../css/template.css">
        <title>'''
final += newDict['title'] + "</title>"
final += '''
    </head>
    <body>
		<nav class="navBar">
			<a href="../../../../login/homepage.html" id="home"> Wiffle </a>
			<ul class="navBarRight">
				<li> <a href="../../../../list.py"> Sites Directory
				</a> </li>
				<li> <a href="about.html"> About Us </a> </li>
'''
final += "<li> <a href='../../../../usersites.py?user="
final += key
final += "'>" + key
final += '''
				</a> </li>
			</ul>
		</nav>
		
        <script src="../../../../js/jquery-2.1.1.min.js"></script>
		<script src="../../../../js/master.js"></script>
		
            <h1 id="headingO" class="s1">
'''
final += newDict["heading"]
final += '''
</h1>
			<div id="sBO">
				<h1 id="sB-nameO">
'''
final += newDict['sB-name'] + "<br>"
final += '''</h1>
				
				<br><br>
				<div id="sBInputO">'''
final += sidebar
final += '''
			</div>
            <!--Main body of the text. Plain text for now-->
            <div id="m-textO" class="s1">
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
        <link rel="stylesheet" href="css/template.css">
        <title>'''
final2 += newDict['title'] + "</title>"
final2 += '''
    </head>
    <body>
		<nav class="navBar">
			<a href="login/homepage.html" id="home"> Wiffle </a>
			<ul class="navBarRight">
				<li> <a href="list.py"> Sites Directory
				</a> </li>
				<li> <a href="about.html"> About Us </a> </li>
'''
final2 += "<li> <a href='usersites.py?user="
final2 += key
final2 += "'>" + key 
final2 +='''
				</a> </li>
			</ul>
		</nav>
		
        <script src="js/jquery-2.1.1.min.js"></script>
		<script src="js//master.js"></script>
		
            <h1 id="headingO" class="s1">
'''
final2 += newDict["heading"]
final2 += '''
</h1>
			<div id="sBO">
				<h1 id="sB-nameO">
'''
final2 += newDict['sB-name'] + "<br>" 
final2 += '''</h1>
				
				<br><br>
				<div id="sBInputO">'''

final2 += sidebar
final2 += '''
			</div>
            <!--Main body of the text. Plain text for now-->
            <div id="m-textO" class="s1">
            '''
final2 +="<pre>" +  output + "</pre>" 
final2 += '''
			
			</div>
'''
final2 +='''
    </body>
</html>
'''




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
    p.write("site0;site0")
    p.close()

'''
tyruf = open("users/" + key + "/sites/exist.txt", "r'")
tyrug = tyruf.readlines()
tyruf.close()

last = tyrug[-1]
#print last
new = "site" + str((int(last[(last.find("e")+1):last.find(";")])) + 1)
newK = new +  ";"+newDict['title']
    

f = open("users/"+ key +"/sites/exist.txt", "a")

if new == "site1":
    f.write("\n")
f.write(newK +"\n")
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
