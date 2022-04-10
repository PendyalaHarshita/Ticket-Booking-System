import socket 
import sys
import os
import struct           
s = socket.socket()        
print ("Socket successfully created")
port = 12345               
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen()    
print ("socket is listening")     
f = open("Ticket.txt", "w")  
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send('Thank you for connecting'.encode())
  msg = c.recv(1024)
  while msg:
    f.write(msg.decode()) 
    msg = c.recv(1024)
  f.close() 
  content = open("Ticket.txt", "rb")
  l=content.read(1024)
  s.send(l)
  c.close()
  break