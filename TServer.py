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
        
        print(threading.currentThread().name, 'start working')
        
        #%% if signin success, break
        while True:
            try:    
                
                account_msg = str(self.socket.recv(1024), encoding='Big5')
                print(account_msg)
                account_msg = handle(account_msg)
                
                if account_msg['type'] == 'account':
                    
                    print('test1')
                    user = AccountManage(account_msg['account'], account_msg['password'])
                    if account_msg['mov'] == 'regist':          #if sign up
                        
                        if_sus_signup = user.signup(account_msg['username'])
                        print(if_sus_signup)
                        if if_sus_signup:
                            print('Signup Success')
                            sus_signup_msg = 'account regist success ' + user.username
                            self.socket.sendall(sus_signup_msg.encode('Big5'))
                            
                        else:
                            print('Signup Fail')
                            fail_signup_msg = 'account regist fail'
                            self.socket.sendall(fail_signup_msg.encode('Big5'))
                            
                        continue
                    
                    elif account_msg['mov'] == 'signin':
                        
                        if_sus_signin = user.signin()
                        if if_sus_signin:
                            print('Signin Success')
                            sus_signin_msg = 'account signin success ' + user.username
                            self.socket.sendall(sus_signin_msg.encode('Big5'))
                            break
                        
                        else:
                            print('Signin Fail')
                            fail_signin_msg = 'account signin fail'
                            self.socket.sendall(fail_signin_msg.encode('Big5'))
                            continue
            
            except Exception():
                self.socket.close()
                print(threading.currentThread().name, 'disconnect')
                return
        
        print('you can start to use mission system')
# =============================================================================
#         #%% only for test
#         c_message = str(self.socket.recv(1024), encoding='Big5')
#         print('Client message is:', c_message)
#         
#         s_message = '我在這'
#         self.socket.send(s_message.encode('Big5'))
#         
#         self.socket.close()
# =============================================================================
