import socket, sys, threading
from threading import Thread # for testing multi-thread
from time import sleep #for sleep in thread
import tkinter as tk
from tkinter import ttk, scrolledtext, END
LocalHost = "127.0.0.1"
SocketChat_PortNumber = 24000

class TextChat():
    def __init__(self, role):
        global hostAddr
        # Create instance
        self.win = tk.Tk()
        self.myRole = role # "Server" or "Client"
        # Add a title
        self.win.title("Python Socket-based TextChatt ({})".format(self.myRole))
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname)
        print("My ({}) IP address = {}".format(self.myRole, hostAddr))
        self.myAddr = hostAddr
        self.createWidgets()
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.myRole == "Server":
            self.mySocket.bind((hostAddr, SocketChat_PortNumber)) # bind socket to (IP_addr(local_host), port_number)
            self.scrDisplay.insert(tk.INSERT,"TCP server is waiting for a client .... \n" )
            self.mySocket.listen(1)
            self.conn, self.cliAddr = self.mySocket.accept() # cliAddr : (IPaddr, port_no)
            print("TCP Server is connected to client ({})\n".format(self.cliAddr))
            self.scrDisplay.insert(tk.INSERT,"TCP server is connected to client\n" )
            self.scrDisplay.insert(tk.INSERT, "TCP client IP address : {}\n".format(self.cliAddr[0]))
            self.cliAddr_entry.insert(END, self.cliAddr[0])
        elif self.myRole == "Client":
            self.cliAddr = self.myAddr
            self.cliAddr_entry.insert(END, self.myAddr)
            servAddr_str = input("Server IP Addr (e.g., '127.0.0.1') = ")
            self.mySocket.connect((servAddr_str, SocketChat_PortNumber)) # send connect request to TCP server
            self.servAddr = self.mySocket.getpeername()
            print("TCP Client is connected to server ({})\n".format(self.servAddr))
            self.scrDisplay.insert(tk.INSERT,"TCP client is connected to server \n")
            self.scrDisplay.insert(tk.INSERT,"TCP server IP address : {}\n".format(self.servAddr[0]) )
            self.servAddr_entry.insert(END, self.servAddr[0])
            self.conn = self.mySocket
        # Start TCP/IP server in its own thread
        thread_sockRecvMsg = Thread(target=self.sockRecvMsg, daemon=True)
        thread_sockRecvMsg.start()

    def sockRecvMsg(self):
        while True:
            recvMsg = self.conn.recv(512).decode()
            if not recvMsg:
                break
            self.scrDisplay.insert(tk.INSERT,">> " + recvMsg)
        self.conn.close()

    #Exit GUI cleanly; definition of quit()
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def sockSendMsg(self): # from server send message to client
        msgToPeer = str(self.scrTextInput.get(1.0, END))
        self.scrDisplay.insert(tk.INSERT,"<< " + msgToPeer)
        self.conn.send(bytes(msgToPeer.encode()))
        self.scrTextInput.delete('1.0', END) #clear scr_msgInput scrolltext

    def createWidgets(self):
        #######################################
        # Add a frame in self.win
        frame = ttk.LabelFrame(self.win, text="Frame(Socket-based Text Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4)
        #Add a LabelFrame of myAddr, peerAddr, Connect Button in frame
        frame_addr_connect = ttk.LabelFrame(frame, text="")
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)
        # Add labels (myAddr, peerAddr) in the frame_addr_connect
        servAddr_label = ttk.Label(frame_addr_connect, text="Server Addr")
        servAddr_label.grid(column=0, row=0, sticky='W') #
        cliAddr_label = ttk.Label(frame_addr_connect, text="Client Addr")
        cliAddr_label.grid(column=1, row=0, sticky='W') #
        # Add a Textbox Entry widgets (myAddr, peerAddr) in the frame_addr_connect
        self.servAddr = tk.StringVar()
        self.servAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)
        self.servAddr_entry.insert(END, hostAddr)
        self.servAddr_entry.grid(column=0, row=1, sticky='W')
        self.cliAddr = tk.StringVar()
        self.cliAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        #self.cliAddr_entry.insert(END, LocalHost)
        self.cliAddr_entry.grid(column=1, row=1, sticky='W')

        # Add ScrolledText fields of display and input
        scrol_w, scrol_h = 40, 20
        msgDisplay_label = ttk.Label(frame, text="Mesage Display ({})".format(self.myRole))
        msgDisplay_label.grid(column=0, row=1 )
        self.scrDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrDisplay.grid(column=0, row=2, sticky='E') #, columnspan=3
        msgInput_label = ttk.Label(frame, text="Input Text Message ({}) :".format(self.myRole))
        msgInput_label.grid(column=0, row=3 )
        self.scrTextInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scrTextInput.grid(column=0, row=4) #, columnspan=3
        # Add Buttons (cli_send, serv_send)
        txButton = ttk.Button(frame, text="Send Message to Peer", command=self.sockSendMsg)
        txButton.grid(column=0, row=5, sticky='E')
        #Place cursor into the message input scrolled text
        self.scrTextInput.focus()
