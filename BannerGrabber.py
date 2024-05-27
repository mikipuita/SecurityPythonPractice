import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(7)
    print(str(s.recv(1024)).strip('b'))



def main():
    ip = input("Please enter the IP address to scan: ")
    port = input("Please enter the port to scan: ")
    banner(ip, port)

main()
