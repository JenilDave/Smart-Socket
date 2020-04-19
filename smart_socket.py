import socket
s = ""
ip_port = ("127.0.0.1",3333)
online_flag = False

class socket_manager():
    ''' This class deals with creating, disconnecting, and maintaining the socket between client and server. It consists of a inbuilt socket
        monitor which monitors and reports the status whether online or offline globaly to all functions so that they can take action accordingly''' 
    def __init__(self):
        #call method to create connetion
        self.tcp_connection_handler()
        #call socket monitoring method
        self.analyze_tcp_socket()
        pass

    def tcp_connection_handler(self):
        global s
        global ip_port        
        global online_flag
        #start the tcp socket creating procedure
        print("Creating Connection.....\n")
        print("This is IP add & Port No.: ", ip_port)
        #af_inet is for ipv4, #sock_stream(TCP) is for seamless connectivity between client-server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #try to connect to server and return 0 or return -1 and display the error
        try:
            s.connect(ip_port)
            print("Connection Created\n Simulator is ONLINE\n")
            #make online flag true if connected which will be used by other objects as refrence
            online_flag = True
            return 0
        except socket.error as err:
            print("Socket creation failed with error\n",err)
            #make offline flag false and close the connection due to error
            online_flag = False
            s.close()
            return -1                    
    
    def analyze_tcp_socket(self):
        ''' This method acts as a socket monitor which monitors the socket status'''
        global online_flag
        print("\n\n<<<::: Socket Monitor is started :::>>>\n\n")
        #this will be always on
        while True:
            #if online_flag is false means device is offline
            if online_flag == False:
                #try to connect again & if it fails to connect by returning -1, try again in 30 secs
                if self.tcp_connection_handler() == -1:
                    print("\nTrying to connect again\n Simulator is OFFLINE!!\n")
                    sleep(30)
                    online_flag = False
                    continue
                #if connection was created by 0 returned, create online_flag true to indicate device is online
                else:
                    online_flag =True
                #continue the process forever
                pass
