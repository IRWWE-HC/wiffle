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

stor1 = newDict["sB-text"]
stor2 = newDict["sB-link"]
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
'''
def fixstor(x):
    temp = x
    if temp.find("\r") != -1:
        temp = temp.replace("\r", "")
    temp = temp.split("\n")
    return temp

stor3 = fixstor(stor1)
stor4 = fixstor(stor2)

#print stor3
#print stor4

def sidebarify():
    output = ""
    pos = 0
    if len(stor3) != len(stor4):
        output += "Double stuffed"
    else:
        while pos != len(stor3):
            output += "<a href=" + stor4[pos] + ">" + stor3[pso] + "</a>" + "<br>"
            pos += 1
        return output
        
sidebar += sidebarify()
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
