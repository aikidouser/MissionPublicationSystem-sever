#%%
import threading
from MsgHandle import handle
from AccountManage import AccountManage

#%%
class MyServer(threading.Thread):
    
    def __init__(self, c_socket, c_adr):
        
        threading.Thread.__init__(self)
        self.socket = c_socket
        self.address= c_adr
        
    def run(self):
        
        print('do somethin')
        
# =============================================================================
#         c_message = str(self.socket.recv(1024), encoding='Big5')
#         print('Client message is:', c_message)
#         
#         s_message = '我在這'
#         self.socket.send(s_message.encode('Big5'))
#         
#         self.socket.close()
# =============================================================================
