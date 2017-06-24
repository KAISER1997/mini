import urllib
from HTMLParser import HTMLParser







class LinkFinder(HTMLParser):
	uncoverd=set()
	coverd=set()
 	def handle_starttag(self,tag,attr):
 		if tag=='a':
 			for attribute,value in attr:
 				if attribute=='href':
 					if value in self.coverd:
 						pass
 					else:
 						self.uncoverd.add(str(value))





	 
    
adi=LinkFinder()
#adi.feed('<img src="python-logo.png" alt="The Python logo">')
q=urllib.urlopen("https://thenewboston.com/videos.php?cat=16").read()
adi.coverd.add("https://thenewboston.com/videos.php?cat=16")
adi.feed(q)
z=0
for x in adi.uncoverd:
	if x=='#' or x in adi.coverd:
		pass
	else:


	    v=urllib.urlopen(str(x))
	    adi.coverd.add(str(x))
	    #adi.uncoverd.remove(str(x))
	    adi.feed(str(v))
	    z=z+1
	    if z==15:
		    break
for x in adi.coverd:
	print x
	

	 