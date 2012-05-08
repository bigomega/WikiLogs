#Initialize a class for storing url and their count
for line in open("log"):
	print line,
	"""
	val=line.find('GET')+4
	if(val==3):
		val=line.find('POST')+5
	print val
	end=line.find(' ',val,val+10)
	print end
	"""
#This is an efficient way, yet i just have to create a string from start and end positions
#The +3 and +4 doesnt look professional and this is not easily scalable for other http methods
	"""
	flag=0
	for word in line.split():
		if(flag==1):
			print word
			break
		if(word=="(GET" or word=="GET" or word=="(POST" or word=="POST"):
			flag=1
	"""
#This is not an efficient way since we have to check each and every word and a good coder doesnt use flags
#and if the method is not detached(eg:"(POST /r/") ie without a space, work becomes tedious
	part=""
	if (len(line.split('GET'))==2):
		part=line.split('GET')[1]
	elif(len(line.split('POST'))==2):
		part=line.split('POST')[1]
	if(part):
		url=part.split()[0]
		print url
		#The storing operations here
		
#Sort the objects based on the ascending order of count
#Store it in a file in the order for retrival purposes
#Template- URL count \ns
