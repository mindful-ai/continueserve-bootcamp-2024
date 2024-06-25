import socket
import threading
import os
os.chdir(r"C:\Users\Purushotham\Desktop\oracle_july\day_05\network_ex")
def RetrFile(name, sock):
    filename = sock.recv(1024)
    print(filename)
    print(filename.decode())
    print(os.path.isfile(filename.decode()))
    if os.path.isfile(filename.decode()):
        message = "EXISTS " + str(os.path.getsize(filename.decode()))
        sock.send(bytes(message, 'utf-8'))
        userResponse = sock.recv(1024)
        if userResponse[:2].decode() == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send(bytes("ERR ", 'utf-8'))

    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print ("Server Started.")
    while True:
        c, addr = s.accept()
        print ("client connected ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()

    s.close()

if __name__ == '__main__':
    Main()
