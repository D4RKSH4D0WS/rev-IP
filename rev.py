#Author D4RKSH4D0WS
#YANG RIKOD GOBLOK, GK MAU BELAJAR YA LO KONTOL !
import requests as r
import os
os.system('clear')
print ('''\033[1;32m_____ _____ __ __ _____ _____  __ _____   __ _____
||_// ||==  \\\ // ||==  ||_// ((  ||==    || ||_//
|| \\  ||___  \V/  ||___ || \\\\ _)) ||___   || ||
''')
try:
	ip=input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mMasukkan IP target : ')
	if ip == '':
		exit('[!] Bye goblok !')
	file=input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mSimpan : ')
	if file == '':
		exit('[!] Bye goblok !')
	site=r.get('http://api.hackertarget.com/reverseiplookup/?q='+ip)
	if 'error' in site.text:
		exit('[!] Masukkan IP dengan benar')
	open(file,"a+").write(site.text+"\n")
	print ('[>] Done\n[>] Tersimpan di',file)
except KeyboardInterrupt:
	exit('\n[!] Keluar')
except r.exceptions.ConnectionError:
	exit('[!] Cek internet lu')

