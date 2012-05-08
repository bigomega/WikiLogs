import os

#Initialize a class for storing url and their count
class urlHits():
		url=""
		count=0
		def __init__(self,url,cnt):
			self.url=url
			self.count=cnt
		def __cmp__(self,urlHit):
			return cmp(self.count,urlHit.count)
		#for object sorting, the cmp operation must be between the count value

def analyseLog(listName,logName):
	urlList=list() #Creates an empty list
	for line in open(listName):
		if(len(line.split())>2):
			urlList.append(urlHits(line.split()[2],int(line.split()[0])))
	#Reads the file and gets the previous hit list and adds them to the urlList as urlHits objects
	for line in open(logName):
		part=""
		if (len(line.split('GET'))==2):
			part=line.split('GET')[1]
		elif(len(line.split('POST'))==2):
			part=line.split('POST')[1]
		if(part):
			url=part.split()[0]
			#Flag for checking if the url is no already present in the list
			flag=0 
			#The storing operations here
			for item in urlList:
				if(item.url==url):
						item.count+=1
						flag=1 #if present just add count
						break
			if(flag==0):
				if(url.startswith('/r/')):
					urlList.append(urlHits(url,1))
	#Sort the objects based on the ascending order of count
	#Store it in a file in the order for retrival purposes
	urlList.sort(None,None,True) #also sorts in reverse
	f=file(listName,'w')
	for item in urlList:
		f.write(str(item.count))
		f.write(" - ")
		f.write(item.url)
		f.write("\n") 
	#Template- "count - URL \n" s
	f.close()

#For headers
fil=file("List.log",'w')
#fil.write("-----------------------------------------------------------------------------------------\nCount - URL\n------------------------------------------------------------------------------------------\n")
fil.close()
#print str(os.getcwd())
for x in os.listdir("logs/"):
	x="logs/"+x
	analyseLog("List.log",x)
#The log files being inside a folder named "logs" in the directory of this python file
#Sample time taken for execution: 8 minutes 26.692 seconds

