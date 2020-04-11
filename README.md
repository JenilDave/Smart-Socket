PLEASE OPEN IN A GOOD TEXT EDITOR



# Smart-Socket
Using Python a Smart Socket is created which will prevent your project to break due to network issues rather will stay on and monitor socket. If socket breaks it will try to connect again.
You need to use Except logic at line 32.
Socket object is declared as s which is global. This project will only work if implemented as a single independent thread.
Example Code:
#code starts here:

from threading import Thread

'''JUST COPY PASTE HERE FROM PY FILE(smart_socket.py)'''

Thread(target= socket_manager).start()

def start_socket_communication():
  try:
    if online_flag == True:
      s.send('HI') #whatever is your message
      return 0 
  except socket.error as err:
      print("Data couldnt be sent due to exception raised:\n", err)
      online_flag = False
      return -1
#similarly for recieving data:
  try:
    if online_flag == True:
      s.recv(1024)
      return 0 
  except socket.error as err:
      print("Data couldnt be recieved due to exception raised:\n", err)
      online_flag = False
      return -1
      
#example code ends here
