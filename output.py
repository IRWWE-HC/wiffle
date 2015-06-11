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

sB = {}

def fix():
    pos = 0
    while True:
        key = "sB-text" + str(pos)
        keyd = "sB-link" + str(pos)
        try:
            sB[newDict[key]] = newDict[keyd]
        except:
            break
        pos += 1
                    
fix()
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
    for i in sB.keys():
        output += "<li> <a href=" + sB[i] + ">" + i + "</a>" + "<br> </li>"
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
        <link rel="stylesheet" href="../../css/css-t1.css">
        <title> Website (Fix later) </title>
    </head>
    <body>
        <script src="../../js/jquery-2.1.1.min.js"></script>
		<script src="../../js/newLink.js"></script>
                <nav class="navBar">
			<a href="../../selector.py" id="home"> Website Editor </a>
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
            <div id="m" class="s1">
            '''
final += output
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
            <div id="m" class="s1">
            '''
final2 += output
final2 += '''
			
			</div>
            <br>
            <a href ="sites"> Sites </a>
            Created by:
'''
final2 += key
final2 +='''
    </body>
</html>
'''

f = open("sites/exist.txt", "r'")
g = f.readlines()
f.close()

last = g[-1]
print last
new = "site" + str((int(last[(last.find("e")+1):])) + 1)



f = open("sites/exist.txt", "a")

if new == "site1":
    f.write("\n")
f.write(new +"\n")
f.close()

os.mkdir("sites/"+new)
y = open("sites/"+ new +"/index.html","w")
y.write(final)
os.chmod("sites/"+ new, 0777)
y.close()

k = open("sites/"+new+"/users.txt","w")
k.write(key +"\n")
k.close()

print final2
