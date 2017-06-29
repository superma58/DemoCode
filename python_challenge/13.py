#www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

#hard clue: 
#www.pythonchallenge.com/pc/return/evil3.jpg open in IE. You can get info:Bert is the evil.
sv = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
sv.phone('Bert')  #555-ITALY