from socket import *
from datetime import datetime
from random import random
#thirren datetime dhe random per realizimin e metdave qe do i kemi me posht dhe qe nuk realizohen pa to

#konverto metoda me ane te if
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
  return "Parametrat ose nenkomandat nuk jane mire !"





#metoda e faktorielit per shprehje
def faktoriel(a):
 h=1;
 num=int(a[0])
 if(num==0):
  return 0
 elif(num>0):
  for x in range(num):
   h=h*(x+1)
 else:
  return "numri duhet te jet pozitiv" 
 return h
 #metoda kenooo
def keno(u=0):
 arr=[]
 for x in range(20):
  arr.append(int((100*random())%80))
 return str(arr)[1:-1] 
 
#metoda e zanoreve 
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
#metoda printo
def printo(text=''):
 text=''.join(text)
 if(text==""):
  return ""
 else:
  return text
#metoda datetime
def time(d=0):
 return str(datetime.now())[:-7]


 

dict={"KONVERTO":konverto,'PRINTO':printo,"ZANORE":zanore,"FAKTORIEL":faktoriel,"TIME":time,"KENO":keno}
def serv(para,dyta):
 
 mesazhiid="Kerkesa nuk u arrit !"
 
 try:
  if(com.upper()=="PORT"):
   mesazhiid=str(adresa[1])   
   para.send(mesazhiid.encode("ASCII"))
   return
  elif(com.upper()=="HOST"):
   mesazhiid=str(adresa[0])
   para.send(mesazhiid.encode("ASCII"))
   return
  else: 
   mesazhiid=str(dict[com.upper()](par))
 except NameError:
  mesazhiid="Komanda nuk eshte e shkruar mire !"
 except TypeError:
  mesazhiid="Parametrat e dhene jane gabim !\n Ju lutem shikoni parametrat\n para se te provoni perseri!!"
 except Exception:
  mesazhiid="Komandat nuk jane mir ose parametrat\nShiko:\nSintaksa e kerkeses duhet te:\nKOMANDA <NENKOMANDA NESE KA> PARAMETRI/AT\n sigurohuni qe parametrat i korespondojn komandave"   
 finally:
  print("mesazhi i derguar: "+mesazhiid)
 para.send(mesazhiid.encode("ASCII")) 
  





serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',9000))
serverSocket.listen()
while True:
 print("Soketa e ra u hap\n")  
 client,clientAddress=serverSocket.accept()
 while True:
  message=client.recv(1024).decode("ASCII")
  print("Mesazhi i pranuar: "+message)
  umorr=message.split(" ")
  umo=umorr[0]
  if(umo=="exit" or com=="quit"):
   client.shutdown(1)
   break
  else:
   par=umorr[1:]
   serv(client,clientAddress)
 
 
