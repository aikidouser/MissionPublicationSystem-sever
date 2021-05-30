#%%
import threading
from MsgHandle import handle
from AccountManage import AccountManage
from MissionManage import MissionManage

#%%
class MyServer(threading.Thread):
    
    def __init__(self, c_socket, c_adr):
        
        threading.Thread.__init__(self)
        self.socket = c_socket
        self.address= c_adr
        
    def run(self):
        
        print(threading.currentThread().name, 'start working')
        
        try:
            #%% if signin success, break
            while True:
                    
                account_msg = str(self.socket.recv(1024), encoding='Big5')
                account_msg = handle(account_msg)
                
                if account_msg['type'] == 'account':
                    
                    user = AccountManage(account_msg['account'], account_msg['password'])
                    if account_msg['mov'] == 'regist':          #if sign up
                        
                        signup_msg = user.signup(account_msg['username'])
                        self.socket.sendall(signup_msg.encode('Big5'))
                        continue
                    
                    elif account_msg['mov'] == 'signin':
                        
                        signin_msg = user.signin()
                        if 'success' in signin_msg:
                            self.socket.sendall(signin_msg.encode('Big5'))
                            break
                        
                        else:
                            self.socket.sendall(signin_msg.encode('Big5'))
                            continue
                        
            print('client can start to use mission system')
            
            #%% Mission System
            while True:
                    
                    mission_msg = str(self.socket.recv(1024), encoding='Big5')
                    mission_msg = handle(mission_msg)
                    
                    if mission_msg['type'] == 'mission':
                        
                        mission = MissionManage()
                        #mission create 
                        if mission_msg['mov'] == 'create':          
                            
# =============================================================================
#                             if_sus_create = mission.create(mission_msg['missionname'], mission_msg['destination'], 
#                                                            mission_msg['deadline'], mission_msg['salary'], 
#                                                            mission_msg['content'], user.username)
# =============================================================================
                            create_msg = mission.create(mission_msg, user.username)

# =============================================================================
#                             if if_sus_create:
#                                 print('Mission Create Success')
#                                 sus_create_msg = 'mission create success ' + mission.missionname
# =============================================================================
                            self.socket.sendall(create_msg.encode('Big5'))
    
                            continue
                        
                        #%% mission search
                        elif mission_msg['mov'] == 'search':
                            
                            search_msg = mission.search(user.username, mission_msg['agp'])
# =============================================================================
#                             if_sus_search = mission.search(user.username, mission_msg['agp'])
#                             if if_sus_search:
#                                 print('Mission Search Success')
#                                 if mission.missionsearch == '':
#                                     mission.missionsearch = ' no results'
#                                 sus_search_msg = 'mission search' + mission.missionsearch
#                                 self.socket.sendall(sus_search_msg.encode('Big5'))
#                             elif if_sus_search:
#                                 print('Mission Search Fail')
#                                 sus_search_msg = 'mission search no results'
#                                 self.socket.sendall(sus_search_msg.encode('Big5'))
# =============================================================================
                            self.socket.sendall(search_msg.encode('Big5'))
                            
                            continue
    
                        #%% mission detail
                        elif mission_msg['mov'] == 'detail':
                            
                            detail_msg = mission.detail(mission_msg['missionname'])
# =============================================================================
#                             if if_sus_detail:
#                                 print('Mission Detail Success')
#                                 if mission.missiondetail == '':
#                                     mission.missiondetail = ' no results'
#                                 sus_detail_msg = 'mission detail' + mission.missiondetail
#                                 self.socket.sendall(sus_detail_msg.encode('Big5'))
#                             elif if_sus_detail:
#                                 print('Mission Detail Fail')
#                                 sus_detail_msg = 'mission detail no results'
#                                 self.socket.sendall(sus_detail_msg.encode('Big5'))
# =============================================================================
                            self.socket.sendall(detail_msg.encode('Big5'))
                            continue
    
                        #%% mission get
                        elif mission_msg['mov'] == 'get':
                            
                            get_msg = mission.get(user.username, mission_msg['missionname'])
# =============================================================================
#                             if if_sus_get:
#                                 print('Mission Get Success')
#                                 sus_get_msg = 'mission get ' + mission_msg['missionname'] + ' success'
#                                 self.socket.sendall(sus_get_msg.encode('Big5'))
#                             elif if_sus_get:
#                                 print('Mission Get Fail')
#                                 sus_get_msg = 'mission get fail'
#                                 self.socket.sendall(sus_get_msg.encode('Big5'))
# =============================================================================
                            self.socket.sendall(get_msg.encode('Big5'))
                            continue
    
                        #%% mission complete
                        elif mission_msg['mov'] == 'complete':
                            
                            complete_msg = mission.complete(user.username, mission_msg['missionname'])
# =============================================================================
#                             if_sus_complete = mission.complete(user.username, mission_msg['missionname'])
#                             if if_sus_complete:
#                                 print('Mission Complete Success')
#                                 sus_complete_msg = 'mission complete ' + mission_msg['missionname'] + ' success'
#                                 self.socket.sendall(sus_complete_msg.encode('Big5'))
#                             elif if_sus_complete:
#                                 print('Mission Complete Fail')
#                                 sus_complete_msg = 'mission complete fail'
#                                 self.socket.sendall(sus_complete_msg.encode('Big5'))
# =============================================================================
                            self.socket.sendall(complete_msg.encode('Big5'))
                            continue
        
        #%% disconnect
        except Exception():
            self.socket.close()
            print(threading.currentThread().name, 'disconnect')
            return  
