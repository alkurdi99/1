""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

import os,sys,time
from time import sleep
os.system('clear')
lib = input(
    '''\033[1;92m

(1) Download lib & update
(2) pass

(⌯) Please Choose : '''
)

if lib == '1':
    os.system('pip install requests')
    time.sleep(1)
    os.system('clear')
    os.system('pip install user_agent')
    time.sleep(1)
    os.system('clear')
    os.system('pip install pycurl')
    time.sleep(1)
    os.system('clear')
    os.system('pip install names')
    time.sleep(1)
    pass
else:
    os.system('clear')
    pass
  

import os , sys , time , requests , json , re , user_agent , pycurl , random , hashlib , names
from time import sleep
from user_agent import generate_user_agent


A = '\033[1;91m'
B = '\033[1;90m'
C = '\033[1;97m'
E = '\033[1;92m'
H = '\033[1;93m'
K = '\033[1;94m'
L = '\033[1;95m'
M = '\033[1;94m'

""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

def baner():
	banera ="""\033[1;92m
	
     888     888 8888888b.       Y88b   d88P 
     888     888 888   Y88b       Y88b d88P  
     888     888 888    888        Y88o88P   
     888     888 888   d88P         Y888P    
     888     888 8888888P"          d888b    
     888     888 888      888888   d88888b   
     Y88b. .d88P 888              d88P Y88b  
      "Y88888P"  888             d88P   Y88b 
                    
\033[1;93m < \033[1;92mTHE SCRIPT INSTA UP  \033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""                  
	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
	
	
	
def following():
	os.system('clear');baner()
	file = "account.txt"
	os.system(f"rm -rf {file}")
	target = input(C+" ("+E+"⌯"+C+") "+C+ "Username Following  : "+E)
	os.system('clear');baner()
	try:
		sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
	except KeyError:
		print (H+" </>  PLEASE LOGIN FIRST.... ")
		os.sys.exit()
	
	
	def git_id():
		os.system("rm -rf id.txt")
		url = 'https://www.instagram.com/{}/?__a=1'.format(target)
		header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+str(sessionid),
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'user-agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
		response = requests.get(url, headers=header)
		idd = str(response.json()['graphql']['user']['id'])
		open('id.txt','a').write(str(idd)+"\n")
		
	git_id()
	try:
		sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
	except KeyError:
		print (H+" </>  PLEASE LOGIN FIRST.... ")
		os.sys.exit()
	cookies = {"sessionid": sessionid,}
	print  (E + " [~] USERNAME  ...\t " + A+target)
	
	headers = {
	'Host': 'www.instagram.com',
	'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'X-IG-App-ID': '936619743392459',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Referer': 'https://www.instagram.com/'+str(target)+'/following/',
	'TE': 'Trailers'}
	
	sidraelezz = 0
	sidratools = 0
	idd = open("id.txt", "r").readline().split('\n')[0]
	response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":false,"first":50}',headers=headers,cookies=cookies)
	while True:
		if str('"has_next_page":false,') in response.text:
			try:
				reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
				for iu in reg:
					sidraelezz += 1
					print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
					open("account.txt","a").write(iu['node']['id']+'\n')
					
					
				print(E+"["+C+"⌯"+E+"] "+A+" Finished")
				input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
				break
			except KeyboardInterrupt:
				print(E+"["+C+"⌯"+E+"] "+A+" Finished")
				input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
				break
		else:
			if sidratools != 0:
				try:
					end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
					response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":false,"first":50,"after":"'+end[0]+'"}',headers=headers,cookies=cookies)
					reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
					for iu in reg:
						sidraelezz += 1
						print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
						open("account.txt","a").write(iu['node']['id']+'\n')
				except KeyboardInterrupt:
					print(E+"["+C+"⌯"+E+"] "+A+" Finished")
					input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
					break
			else:
				try:
					reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
					for iu in reg:
						sidraelezz += 1
						print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
						open("account.txt","a").write(iu['node']['id']+'\n')
						
				except KeyboardInterrupt:
					print(E+"["+C+"⌯"+E+"] "+A+" Finished")
					input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
					break
				sidratools += 1
				
				
				
		
def followers():
	os.system('clear');baner()
	file = "account.txt"
	os.system(f"rm -rf {file}")
	target = input(C+" ("+E+"⌯"+C+") "+C+ "Username Followers  : "+E)
	os.system('clear');baner()
	try:
		sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
	except KeyError:
		print (H+" </>  PLEASE LOGIN FIRST.... ")
		os.sys.exit()
	
	
	def git_id():
		os.system("rm -rf id.txt")
		url = 'https://www.instagram.com/{}/?__a=1'.format(target)
		header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+str(sessionid),
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'user-agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
		response = requests.get(url, headers=header)
		idd = str(response.json()['graphql']['user']['id'])
		open('id.txt','a').write(str(idd)+"\n")
		
	git_id()
	try:
		sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
	except KeyError:
		print (H+" </>  PLEASE LOGIN FIRST.... ")
		os.sys.exit()
	cookies = {"sessionid": sessionid,}
	print  (E + " [~] USERNAME  ...\t " + A+target) 
	
	headers = {
	'Host': 'www.instagram.com',
	'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)",
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'X-IG-App-ID': '936619743392459',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Referer': 'https://www.instagram.com/'+str(target)+'/followers/',
	'TE': 'Trailers'}
	
	sidraelezz = 0
	sidratools = 0
	idd = open("id.txt", "r").readline().split('\n')[0]
	response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":true,"first":50}',headers=headers,cookies=cookies)
	while True:
		if str('"has_next_page":false,') in response.text:
			try:
				reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
				for iu in reg:
					sidraelezz += 1
					print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
					open("account.txt","a").write(iu['node']['id']+'\n')
					
					
				print(E+"["+C+"⌯"+E+"] "+A+" Finished")
				input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
				break
			except KeyboardInterrupt:
				print(E+"["+C+"⌯"+E+"] "+A+" Finished")
				input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
				break
		else:
			if sidratools != 0:
				try:
					end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
					response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+str(idd)+'","include_reel":true,"fetch_mutual":true,"first":50,"after":"'+end[0]+'"}',headers=headers,cookies=cookies)
					reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
					for iu in reg:
						sidraelezz += 1
						print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
						open("account.txt","a").write(iu['node']['id']+'\n')
				except KeyboardInterrupt:
					print(E+"["+C+"⌯"+E+"] "+A+" Finished")
					input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
					break
			else:
				try:
					reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
					for iu in reg:
						sidraelezz += 1
						print(E+"["+C+f" {sidraelezz} "+E+"] "+str(iu['node']['id']))
						open("account.txt","a").write(iu['node']['id']+'\n')
						
						
				except KeyboardInterrupt:
					print(E+"["+C+"⌯"+E+"] "+A+" Finished")
					input(E+"["+C+"⌯"+E+"] "+C+" plass Enter To Continue.....")
					break
				sidratools += 1
				
				
				

def Instaup():
	os.system('clear');baner()
	ok = 0
	sk = 0
	userid = int(input(E+"("+C+"⌯"+E+") "+C+" USER ID "+A+" : "+E))
	token = input(E+"("+C+"⌯"+E+") "+C+"TOKEN BOT :\n==> "+C)
	ID = input(E+"("+C+"⌯"+E+") "+C+"ID TELEGRAM  :"+C)
	userss = len(open('account.txt','r').read().splitlines())
	print (E+"("+C+"⌯"+E+") "+C+"Number Of Ids : "+E+str(userss))
	print (50 * '\033[1;92m~')
	id = open("account.txt","r").readlines()
	for run in id:
		if str(sk)==200:
			print ("\n Threading tools  ..")
			
			
		uid = run.strip()
		use ='1234567890qwertyuioplkjhgfdsazxcvbnm'
		uss = '0987654321'
		us = str("".join(random.choice(use)for i in range(16)))
		ua = str("".join(random.choice(use)for i in range(40)))
		a1 = str("".join(random.choice(uss)for i in range(2)))
		a2 = str("".join(random.choice(uss)for i in range(2)))
		a3 = str("".join(random.choice(uss)for i in range(2)))
		a4 = str("".join(random.choice(uss)for i in range(2)))
		name1 = names.get_first_name()
		name2 = names.get_first_name()
		nemes = str(name1)+str(a1)+str(name2)+str(a2)
		tim = time.time()
		IP_address = '{}.{}.{}.{}'.format(str(a1),str(a2),str(a3),str(a4))
		data = 'market=Bazaar&user_id=' + uid + '&iad=' + ua + '&user_name=' + nemes
		account = hashlib.md5(b'45:8D:2E:5C:3A:B4:02:2D:B5:DD:3B:E0:98:4F:14:90:CB:5F:B5:45' + bytes(uid, 'utf-8')).hexdigest()
		url = 'https://instaup.marsapi.com/get_likes/user/coins'
		home = 'null/02:00:00:00:00:00/'+str(tim)+'/'+str(us)+'/null/'+str(us)
		headers = [
        'market: Bazaar',
        'access: ' + account,
        'lng: en',
        'api_key: ABCXYZ123TEST',
        'Nagent: '+home,
        'cnt: unknown',
        'version: 51',
        'pkg: f2c6d7a5b030a1542f7eb589d5013340',
        'aid: ' +ua,
        'Content-Type: application/x-www-form-urlencoded',
        'Host: instaup.marsapi.com',
        'Connection: Keep-Alive',
        'Accept-Encoding: gzip',
        'User-Agent:'+generate_user_agent(),
        'X-Forwarded-For: ' + IP_address]
        
		sidra = pycurl.Curl()
		sidra.setopt(pycurl.URL, url)
		sidra.setopt(pycurl.POST, 1)
		sidra.setopt(pycurl.POSTFIELDS, data)
		sidra.setopt(pycurl.HTTPHEADER, headers)
		sidra.setopt(pycurl.SSL_VERIFYPEER, False)
		sidra.setopt(pycurl.ENCODING, 'gzip')
		responsa = sidra.perform_rs()
		sidra.close()
		if ('@gmail.com') in responsa:
			ok+=1
			print(E+"("+C+str(ok)+E+") "+H+"CHECK COIN "+H+"==>"+C+" IP address block Wait 30 Minutes ")
			sleep(300)
		
		elif ('{"coins":') in responsa:
			coins = str(responsa.split('coins":"')[1])
			coine = str(coins.split('"')[0])
			coina = int(coine)
			ordera = (coina/4)
			ordere = str(ordera)
			orders = ordere.split('.')[0]
			sk+=1
			sleep (40)
			
           #-------->-------------------------------------------------------------------------
           #-------->- Cod BY : SidraELEzz
           #-------->- Github : https://github.com/SidraELEzz
           #-------->- Telegram: https://t.me/SidraTools
           #-------->- Telegram: https://t.me/tt_rq
           #-------->-------------------------------------------------------------------------
      

			
			#--------> send followers 
			
			
			
			print(E+"("+C+str(sk)+E+") "+H+"CHECK COIN "+H+"==> "+E+str(coine))
			
			if int(coine) >1000 or int(coine) > 800 or int(coine) > 400 or int(coine) > 200:
				url = "https://script-new-up.herokuapp.com/?target={}&userid={}&order={}&submit=submit".format(uid,userid,orders)
				headers = {
                   "Host": "script-new-up.herokuapp.com",
                   "Connection": "keep-alive",
                   "Cache-Control": "max-age=0",
                   "sec-ch-ua": 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
                   "sec-ch-ua-mobile": "?1",
                   "sec-ch-ua-platform": "Android",
                   "X-Chrome-offline": "persist=0 reason=reload",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": str(generate_user_agent()),
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Sec-Fetch-Site": "none",
                   "Sec-Fetch-Mode": "navigate",
                   "Sec-Fetch-User": "?1",
                   "Sec-Fetch-Dest": "document",
                   "Accept-Encoding": "gzip",
                   "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
                   
				response = requests.request('GET',url,headers=headers)
				if ('Successful') in str(response.text):
					massage=("• Successful Send Followers ✓\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n[💠] ID Target  : "+str(uid)+"\n[👥] Send Followers  : "+str(orders)+"\n[💰] Coin  : "+str(coine)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele ➥• @SidraTools")
					print(C+"("+E+"✓"+C+") "+E+"SUCCESSFUL SEND FOLLOWERS "+C+"==> "+E+str(orders))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
					print ('')
					sleep (20)
					
				elif ('There is a problem registering the order. Contact support') in str(response.text):
					print(C+"["+E+"~"+C+"] "+C+"Wait To Completed Old Orderr")
					print ("")
					sleep (20)
					
				else:
					print(C+"["+E+"~"+C+"] "+C+"DONT SUCCESSFUL SEND FOLLOWERS ")
					print ("")
					sleep (20)
					
				
			else:
				print(C+"["+E+"~"+C+"] "+C+"DONT SUCCESSFUL COIN "+H+"==> "+E+str(coine))
				print ('')
				sleep (20)
			
		else:
			print(C+"["+E+"~"+C+"] "+C+"FALSE COIN ")
			sleep (40)
				
				
			
		
def Instagram():
	os.system('clear');baner()
	file = "sessionid.txt"
	os.system(f'rm -rf {file}')
	sessionid = input(C+" ("+E+"⌯"+C+") "+C+ "SESSIONID ACCOUNT :"+E)
	url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
	headers = {
    'X-IG-Connection-Type':'WIFI',  'X-IG-Capabilities':'3brTBw==', 
    'User-Agent':'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)', 
    'Accept-Language':'en-US', 
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Accept-Encoding':'gzip, deflate', 
    'Host':'i.instagram.com', 
    'Connection':'keep-alive', 
    'Accept':'*/*'}
	cookies = {"sessionid": sessionid} 
	response = requests.get(url,headers=headers,cookies=cookies).json()
	#print (response)
	if str('message') in response:
		print(A+" \n</>  LOGIN  ACCOUNT ERROR ")
		os.system('xdg-open https://t.me/sessionidbot')
		sleep (10)
		Instagram()
		
	else:
		print(E+" \n</>  LOGIN  ACCOUNT SUCCESSFUL ")
		username = str(response['user']['username'])
		
		open("sessionid.txt","a").write(str(sessionid)+'\n')
		sleep (10)
		pass 
			
	os.system('clear');baner()
	print (E+"( "+C+username+E+" )")
	print(A+" ---------------------------") 
	print(E+"("+C+"1"+E+") "+E+" START INSTA UP ")
	print(E+"("+C+"2"+E+") "+C+" GET ID from Followers ")
	print(E+"("+C+"3"+E+") "+C+" GET ID from Following ")
	print(A+" ---------------------------")
	tools = input(E+"("+C+"⌯"+E+") "+C+" CHOOSE GET ID "+A+" : "+E)
	if str(tools) in ["", " "]:
		os.system('xdg-open https://t.me/SidraTools/1')
		os.sys.exit(A+" Error ..... ?! ")
		
	elif str(tools) in ["1", "01"]:
		Instaup()
		
	elif str(tools) in ["2", "02"]:
		followers()
		
		
	elif str(tools) in ["3", "03"]:
		following()
		
		
	else:
		os.system('xdg-open https://t.me/SidraTools/1')
		os.sys.exit(A+" Error ..... ?! ")
	
	
while True:
	Instagram()

#-------->-------------------------------------------------------------------------
#-------->- Cod BY : SidraELEzz
#-------->- Github : https://github.com/SidraELEzz
#-------->- Telegram: https://t.me/SidraTools
#-------->- Telegram: https://t.me/tt_rq
#-------->-------------------------------------------------------------------------
	