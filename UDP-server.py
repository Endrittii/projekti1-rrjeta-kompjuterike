from socket import *
from datetime import datetime
from random import random
#per krijimin e metodave duhet thirrur edhe datetime si dhe random sepse duhet te krijohet kodi dhe inicializimi i tyre 
#metoda e faktorielit
def faktoriel(a):
 b=1;
 num=int(a[0])
 if(num==0):
  return 0
 elif(num>0):
  for x in range(num):
   b=b*(x+1)
 else:
  return "numri duhet te jet pozitiv" 
 return b
#metoda zanore
def zanore(z=""):
 z=''.join(z)   
 a=['a','e','i','o','u','y','A','E','I','O','U','Y']
 num=0;
 if(z==""):
     return 0
 else:
  sli=list(z)
  for x in a:
   num=num+sli.count(x)
 return num    

 #metoda keno
def keno(u=0):
 arr=[]
 for x in range(20):
  arr.append(int((100*random())%80))
 return str(arr)[1:-1] 
 
#metoda printo
def printo(text=''):
 text=''.join(text)
 if(text==""):
  return ""
 else:
  return text
#metoda per datetime
def time(d=0):
 return str(datetime.now())[:-7]
#metoda e cila bene konvertimin 
def konverto(a):
 num=float(a[1])
 if(a[0].upper()=="KTOC"):
   return num-273.16 
 elif(a[0].upper()=="CTOK"):
   return num+273.16
 elif(a[0].upper()=="FTOC"):
   return (num-32)*5/9
 elif(a[0].upper()=="CTOF"):
   return (num*9/5)+32
 elif(a[0].upper()=="FTOK"):
   g=num-32
   c=5/9
   gc=g*c
   return gc+273.16
 elif(a[0].upper()=="KTOF"):
   g=num-273.16
   j=9/5
   gj=g*j
   return  gj+32
 else:
  return "Parametrat nuk jane mir ose edhe nenkomanda!"



 



#dict={'PRINTO':printo,"IP":ip,"PORT":port,"ZANORE":zanore,"HOST":host,"TIME":time,"KENO":keno,"FAKTORIEL":faktoriel,"KONVERTO":konverto}
#qe te arrihet apo jo kemi shprehjet
dict={"KONVERTO":konverto,'PRINTO':printo,"ZANORE":zanore,"FAKTORIEL":faktoriel,"TIME":time,"KENO":keno}
def serv(adresa):
 mesazhiid="Kerkesa nuk u arrit !"
 
 try:
  if(com.upper()=="PORT"):
   mesazhiid=str(adresa[1])   
   serverSocket.sendto(mesazhiid.encode("ASCII"), adresa)
   return
  elif(com.upper()=="HOST"):
   mesazhiid=str(adresa[0])
   serverSocket.sendto(mesazhiid.encode("ASCII"), adresa)
   return
  else: 
   mesazhiid=str(dict[com.upper()](par))
 except NameError:
  mesazhiid="Komanda nuk eshte e shkruar mire!"
 except TypeError:
  mesazhiid="Nuk jane parametrat e dhene si duhet!\n kontrolloni parametrat edhe njehere\n !!"
 except Exception:
  mesazhiid="Komanda ose parametrat gabim\nNdihme:\nSintaksa e kerkeses eshte :\nKOMANDA <NENKOMANDA NESE EKZISTON> PARAMETRI/AT\n shikoni per parametrat se a i'u takojne komandave"   
 finally:
  print("mesazhi i cili eshte derguar: "+mesazhiid)
 serverSocket.sendto(mesazhiid.encode("ASCII"), adresa) 

serverPort=9000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Serveri eshte i gatshem !!")
while True:
 message,clientAddress=serverSocket.recvfrom(1028)
 print("Mesazhi i cili ka ardhur: " + message.decode("ASCII"))
 umorr=message.decode("ASCII").split(" ")
 umo=umorr[0]
 par=umorr[1:]
 serv(clientAddress)


  
