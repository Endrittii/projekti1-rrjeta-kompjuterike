from socket import *

sock=socket(AF_INET,SOCK_DGRAM)
port=int(input("PORT>>"))
ip=input("IP ADDRESS>>")
a=""
while True:
 a=input("Shtyp komandën>>")
 if(a==""):
  break
 sock.sendto(a.encode("ASCII"),(ip,port))
 message,sockadd=sock.recvfrom(1024)
 print("<<<"+message.decode("ASCII")+"\n\n")
print("Soketta u mbyll") 
sock.close() 
