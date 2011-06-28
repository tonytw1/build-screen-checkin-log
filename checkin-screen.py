import commands
import sys
import xml.dom.minidom
from xml.dom.minidom import Node

svnUrl = sys.argv[1]
svnCmd = 'svn log -l 5 --verbose --xml ' + svnUrl
revisionsXml = commands.getoutput(svnCmd)
doc = xml.dom.minidom.parseString(revisionsXml)

print '<html><head><link rel="stylesheet" href="styles.css"></head><body>';
print '<h1>Meanwhile...</h1>';

for revision in doc.getElementsByTagName("logentry"):

    print '<img class="author" src="icons/' + revision.getElementsByTagName("author")[0].firstChild.nodeValue + '.png"/>';
    print '<ul class="revision">';
    print '<li class="date">'
    print revision.getElementsByTagName("date")[0].firstChild.nodeValue
    print '</li>'

    print '<li class="heading">'
    print '#' + revision.getAttribute("revision")
    print '</li>'
    

    print '<li class="msg">'
    print revision.getElementsByTagName("msg")[0].firstChild.nodeValue
    print '</li>'

    print '<ul class="paths">'
    for path in revision.getElementsByTagName("path"):
        print '<li class="path">' + path.firstChild.nodeValue + '</li>';
    print '</ul>'
    print '</li>'
    print '</ul>'

print '</body></html>';
