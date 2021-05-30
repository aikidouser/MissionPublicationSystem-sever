#%%
import json
import threading

#%%
lock = threading.Lock()

#%%
class MissionManage:
    
    def __init__(self):  
        1 == 1
    
    #%% mission create
    def create(self, mission_data, username):

# =============================================================================
#         self.missionname = missionname
#         self.destination = destination
#         self.deadline = deadline
#         self.salary = salary
#         self.content = content
#         self.postname = postname
#         self.getname = 'none'
# 
#         mission_dict = {'missionname' : self.missionname,
#                         'destination' : self.destination,
#                         'deadline' : self.deadline,
#                         'salary' : self.salary,
#                         'content' : self.content,
#                         'postname' : self.postname,
#                         'getname' : self.getname}
# =============================================================================
        mission_data['postname'] = username
        mission_data['getname'] = 'none'        

        lock.acquire()
        try:
            with open ('mission_info.json', 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            data = list()

        with open('mission_info.json', 'w') as json_file:
            data.append(mission_data)
            json.dump(data, json_file)
            
        lock.release()
        
        print('Mission Create Success')
        create_msg = 'mission create success ' + mission_data['missionname']
        
        return create_msg       #mission create Success


    #%% mission search
    def search(self, username, agp):
        
        #self.missionsearch = ''
        search_msg = 'mission search'
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            if agp == 'all':
                for mission in mission_data:
                    if mission['getname'] == 'none':
                        search_msg += ' ' + mission['missionname']
            
            elif agp == 'get':
                for mission in mission_data:
                    if username == mission['getname']:
                        search_msg += ' ' + mission['missionname']
                        
            elif agp == 'post':
                for mission in mission_data:
                    if username == mission['postname']:
                        search_msg += ' ' + mission['missionname']

        except Exception:    
            pass
        
        return search_msg
        

    #%% mission detail
    def detail(self, missionname):
        
        #self.missiondetail = ''
        detail_msg = 'mission detail'
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            for mission in mission_data:
                if missionname == mission['missionname'] and mission['getname'] == 'none':
                    detail_msg = ' ' + mission['missionname'] \
                                 + ' ' + mission['destination'] \
                                 + ' ' + mission['deadline'] \
                                 + ' ' + mission['salary'] \
                                 + ' ' + mission['content']
                    print('Mission Detail Success')
                    return detail_msg

        except Exception:    
            pass
        
        print('Mission Detail Fail')
        return detail_msg + ' fail'

    #%% mission get
    def get(self, username, missionname):
        
        #if_sus_get = False
        get_msg = 'mission get'
        
        lock.acquire()
        
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            for mission in mission_data:
                if username != mission['postname'] and mission['missionname'] == missionname and mission['getname'] == 'none':
                    mission['getname'] = username
                    #if_sus_get = True
                    get_msg += ' success ' + missionname
                    
                    with open('mission_info.json', 'w') as json_file:
                        json.dump(mission_data, json_file)
                    
                    lock.release()
                    print('Mission Get Success')
                    return get_msg

        except Exception:    
            pass
        
        lock.release()
        print('Mission Get Fail')
        return get_msg + ' fail'
# =============================================================================
#         if if_sus_get:
#             return True
#         elif if_sus_get:
#             return False
# =============================================================================
        

    #%% mission complete
    def cmoplete(self, username, missionname):
        
        #if_sus_complete = False
        complete_msg = 'mission complete'
        
        lock.acquire()
 
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            for mission in mission_data:
                if username == mission['getname'] and missionname == mission['missionname']:
                    mission_data.remove(mission)
                    complete_msg += ' ' + missionname
                    
                    with open('mission_info.json', 'w') as json_file:
                        json.dump(mission_data, json_file)
                    
                    lock.release()
                    print('Mission Complete Success')
                    return complete_msg

        except Exception:    
            pass
        
        lock.release()
        print('Mission Complete Fail')
        return complete_msg +' fail'
        
# =============================================================================
#         if if_sus_complete:
#             return True
#         elif if_sus_complete:
#             return False
# =============================================================================
