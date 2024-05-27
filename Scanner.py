import nmap # type: ignore

scanner = nmap.PortScanner()

print("Welcome to the port scanner! This is a simple automation tool")
print("<--------------------------------------------------------->")

ip_addr = input("Please enter the IP address to scan: ")
print("The IP you have entered is: ",  ip_addr)
type(ip_addr)

response = input(""" \nPlease enter the type of scan you want to run 
                 1)SYN ACK Scan
                 2)UDP Scan
                 3)Comprehensive Scan \n""")
print("You have selected option: ", response)

if response == "1": 
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-V -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif response == "2": 
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-V -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif response == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-V -sS -sC -sV -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif response >= '4':
    print("Please enter a valid option")
    
