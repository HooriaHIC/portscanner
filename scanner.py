import socket

host = str(input("Enter host to scan: "))
ip = socket.gethostbyname(host)
print(ip)
while 1:
    try:
        port = int(input("Enter port: "))
        try:
            sock = socket.socket()
            res = sock.connect((ip, port))
            print("Port {}: Available(open)".format(port))
            sock.close()
        except:
            print("Port {}: Unavailable(close)".format(port))
    except ValueError:
        print("please enter a valid port.")
print("Port Scanning completed successfully :)")
