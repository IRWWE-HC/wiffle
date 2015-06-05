#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb

cgitb.enable()
d=cgi.FieldStorage()
sidebar = ""


newDict = {}
for i in d.keys():
    newDict[i] = d[i].value
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
print sB
'''
print stor1
print "<br>"
print stor2
print "<br>"
#print d
print "<br>"
print newDict
print "<br>"
print newDict["title"]
def fixstor(x):
    temp = x
    if temp.find("\r") != -1:
        temp = temp.replace("\r", "")
    temp = temp.split("\n")
    return temp

stor3 = fixstor(stor1)
stor4 = fixstor(stor2)
'''

#print stor3
#print stor4

def sidebarify():
    output = ""
    pos = 0
    for i in sB.keys():
        output += "<a href=" + sB[i] + ">" + i + "</a>" + "<br>"
    return output
        
sidebar += sidebarify()
if 'm-text' in newDict.keys():
    output = sidebar + newDict['m-text'] 
# sB-link

# m-text

def html(x):
    output = ""
    output += "<!DOCTYPE html> <html> <head>"
    output += "<title>" + newDict["title"] + "</title>" 
    output += "</head> <body>"
    #output += "<pre>" 
    output += "<h1> <center> --- </center> </h1>" 
    output += str(x) 
    #output += "</pre>"
    output += "</body> </html>" 
    return output

print html(output)
