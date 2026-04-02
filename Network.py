import socket # imports socket library

class Network:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initializes server object
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initializes client object

        self.conn = 0
        self.addr = 0

    def serverIP(self): # detects host local IP address
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        return IPAddr

    def serverConnect(self, IPAddr): # establishes server connection
        
        self.serv.bind((IPAddr, 8080)) # functional, but needed to specify ip address on client
        self.serv.listen(1)
        self.conn, self.addr = self.serv.accept()

    def serverEnd(self): # closes server connection
        self.serv.close()

    def clientEnd(self): # closes client connection 
        self.client.close()



    def clientConnect(self, IPAddr): # establishes client connection to server
        self.client.connect((IPAddr, 8080))

    def clientNetworkTest(self): # client sends test byte
        test = "1"
        self.client.send(test.encode())

    def serverReceiveTest(self): # server receives test byte
        self.conn.recv(1)

            

            
        


    def serverSend(self, board, move, check, capturedlist):
        boardToSend = ""
        movelogToSend = ""
        checkToSend = ""
        capturedToSend = ""

        # send board

        for i in range(len(board)):
            boardToSend = ""
            arrayToSend = board[i]

            for item in arrayToSend: # converts board to string
                boardToSend = boardToSend + str(item) + " "
            
            boardBytes = len(boardToSend.encode())
            if boardBytes < 10:
                boardBytes = "0" + str(boardBytes) # calculates board bytes length
            self.conn.send(str(boardBytes).encode()) # sends board byte length
            self.conn.send(boardToSend.encode()) # encodes and sends board string
        
        # send move log
        moveBytes = len(move.encode())
        self.conn.send(str(moveBytes).encode()) # sends move byte length
        self.conn.send(move.encode()) # encodes and sends move string

        # send check
        if check == True:
            checkBytes = 4 # sets byte length
            checkToSend = "True "
        else:
            checkToSend = "False "
            checkBytes = 5

        checkBytes = str(checkBytes)

        self.conn.send(checkBytes.encode()) # sends byte length
        self.conn.send(checkToSend.encode()) # sends check value

        # send captured

        for item in capturedlist: # converts captured list to string
            capturedToSend = capturedToSend + str(item) + " "

        capturedBytes = len(capturedToSend.encode()) # calculates captured list byte length

        if capturedBytes < 10: # formats byte length correctly, to always be 3 bytes
            capturedBytes = "0" + str(capturedBytes)
            self.conn.send(capturedBytes.encode())
        elif capturedBytes == 0:
            capturedBytes = "00"
            self.conn.send(capturedBytes.encode())
        else:
            self.conn.send(str(capturedBytes).encode())
        
        self.conn.send(capturedToSend.encode()) # sends captured pieces list


    def serverReceiveBoard(self): # server receives board state


        board = [[],[],[],[],[],[],[],[]]

        for i in range(8):
            bytes = int((self.conn.recv(2)).decode())


            array = []
            str = ""
            str = self.conn.recv(bytes) # receives string, decodes and splits into array

            str = str.decode()
            array = str.split()

            if len(array) != 8:
                str = ""
                str = self.conn.recv(18)
                str = str.decode()
                array = str.split()


            for x in range(len(array)): # converts items to integers
                array[x] = int(array[x])

            board[i] = array

        return board

    def serverReceiveMovelog(self): # server receive move log
        movelogBytes = int((self.conn.recv(1)).decode())
        movelogReceived = (self.conn.recv(movelogBytes)).decode()

        return movelogReceived
        
    def serverReceiveCheck(self): # server receives check status
        checkBytes = int((self.conn.recv(1)).decode())

        checkReceived = (self.conn.recv(checkBytes)).decode()

        if checkReceived == "True":
            check = True
        else:
            check = False

        return check

    def serverReceiveCaptured(self): # server receives captured pieces list
        capturedBytes = int((self.conn.recv(3)).decode())

        capturedReceived = (self.conn.recv(capturedBytes)).decode()
        blackCaptured = capturedReceived.split()

        for item in blackCaptured:
            item = int(item)

        return blackCaptured

    def clientSend(self, board, move, check, capturedlist): # client sends game data
        boardToSend = ""
        movelogToSend = ""
        checkToSend = ""
        capturedToSend = ""

        # send board

        for i in range(len(board)):
            boardToSend = ""
            arrayToSend = board[i]

            for item in arrayToSend:
                boardToSend = boardToSend + str(item) + " "

            boardBytes = len(boardToSend.encode())
            if boardBytes < 10:
                boardBytes = "0" + str(boardBytes)
            self.client.send(str(boardBytes).encode())

            self.client.send(boardToSend.encode())
        
        # send move log

        moveBytes = str(len(move.encode()))
        self.client.send(moveBytes.encode())

        self.client.send(move.encode())


        # send check
        if check == True:
            checkBytes = 4
            checkToSend = "True "
        else:
            checkToSend = "False "
            checkBytes = 5

        checkBytes = str(checkBytes)
        self.client.send(checkBytes.encode())

        self.client.send(checkToSend.encode())


        # send captured

        for item in capturedlist:
            capturedToSend = capturedToSend + str(item) + " "

        capturedBytes = len(capturedToSend.encode())


        if capturedBytes < 10 and capturedBytes > 0:
            capturedBytes = "0" + str(capturedBytes)
            self.client.send(capturedBytes.encode())
        elif capturedBytes == 0:
            capturedBytes = "00"
            self.client.send(capturedBytes.encode())
        else:
            self.client.send(str(capturedBytes).encode())
        
        self.client.send(capturedToSend.encode())




    def clientReceiveBoard(self): # client receives board state

        board = [[],[],[],[],[],[],[],[]]

        for i in range(8):
            bytes = int((self.client.recv(2)).decode())
            array = []
            str = ""
            str = self.client.recv(bytes)  # receives string, decodes and splits into array

            str = str.decode()
            array = str.split()

            if len(array) != 8:
                str = ""
                str = self.client.recv(18)
                str = str.decode()
                array = str.split()



            for x in range(len(array)): # converts items to integers
                array[x] = int(array[x])

            board[i] = array


        return board

    def clientReceiveMovelog(self): # client receives move log list
        movelogBytes = int((self.client.recv(1)).decode()) # receives byte length
        movelogReceived = (self.client.recv(movelogBytes)).decode() # receives and decodes move

        return movelogReceived
        
    def clientReceiveCheck(self): # client receives check status
        checkBytes = int((self.client.recv(1)).decode())

        checkReceived = (self.client.recv(checkBytes)).decode()

        if checkReceived == "True":
            check = True
        else:
            check = False

        return check

    def clientReceiveCaptured(self): # client receive captured pieces list
        capturedBytes = int((self.client.recv(3)).decode())

        capturedReceived = (self.client.recv(capturedBytes)).decode()
        whiteCaptured = capturedReceived.split()

        for i in range(len(whiteCaptured)):
            whiteCaptured[i] = int(whiteCaptured[i])

        return whiteCaptured
