from socket import *

sock=socket(AF_INET,SOCK_STREAM)
port=int(input("PORT>>"))
ip=input("IP ADDRESS>>")
a=""
sock.connect((ip,port))
while True:
 a=input("Shtyp komandën>>")
 sock.send(a.encode("ASCII"))
 message=sock.recv(1024).decode("ASCII")
 if(message=="exit" or message==""):
  print("socket exiting")
  break
 print(message)
sock.close()
print("socketa u mbyll") 
