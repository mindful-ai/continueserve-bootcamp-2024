import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = input("Filename? -> ")
    if filename != 'q':
        s.send(bytes(filename, 'utf-8'))
        data = s.recv(1024)
        print(data)
        if data[:6].decode() == 'EXISTS':
            filesize = int(data[6:].decode())
            message = input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send(bytes("OK", 'utf-8'))
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print ( "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print ("Download Complete!")
                f.close()
        else:
            print ("File Does Not Exist!")

    s.close()
    

if __name__ == '__main__':
    Main()
