alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class urlHits():
		url=""
		count=0
		def __init__(self,url,cnt):
			self.url=url
			self.count=cnt
		def __cmp__(self,urlHit):
			return cmp(self.count,urlHit.count)

def conn(nu):
	ans=""
	qq=nu
	while(qq):
		ans+=alphabet[(qq%36)]
		qq=qq/36
	return ans[::-1]
listt=["/r/nv0","/r/1eg5" ,"/r/33y0","/r/tpn",'/r/']




urlList=list() #Creates an empty list
for line in open('List.log'):
	if(len(line.split())>2):
		urlList.append(urlHits(line.split()[2],int(line.split()[0])))

for ob in urlList:
	if(ob.url.startswith('/r/')):
		if(0<len(ob.url.split('/r/')[1])<5 and (ob.url[-1].isalpha() or ob.url[-1].isdigit())):
			ob.url="http://ta.wikipedia.org/w/api.php?action=query&prop=pageprops&format=json&pageids="+str(int(ob.url.split('/r/')[1],36))
	
f=file('query.txt','w')
for item in urlList:
	f.write(str(item.count))
	f.write(" - ")
	f.write(item.url)
	f.write("\n") 
	#Template- "count - URL \n" s
f.close()

"""
	print len(url)
	if(len(url)>3):
		print url
		if(url[0]=='/' and url[1]=='r' and url[2]=='/'):
			print url.startswith('/r')

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    ""Converts an integer to a base36 string.""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')
 
    if number >= 0 and number <= 9:
        return alphabet[number]
 
    base36 = ''
    sign = ''
 
    if number < 0:
        sign = '-'
        number = -number
 
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
 
    return sign + base36
 
def base36decode(number):
    return int(number, 36)
 
print base36encode(1412823931503067241)
print base36decode('AQF8AA0006EH')
print conn(100000)
print int("aef21", 36)
"""
