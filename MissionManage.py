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
    def create(self, mission_data, account):

        mission_data['postname'] = account
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
    def search(self, account, agp):
        
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
                    if account == mission['getname']:
                        search_msg += ' ' + mission['missionname']
                        
            elif agp == 'post':
                for mission in mission_data:
                    if account == mission['postname']:
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
                if missionname == mission['missionname']:
                    detail_msg += ' ' + mission['postname'] \
                                 + ' ' + mission['missionname'] \
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
    def get(self, account, missionname):
        
        #if_sus_get = False
        get_msg = 'mission get'
        
        lock.acquire()
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            for mission in mission_data:
                if account != mission['postname'] and mission['missionname'] == missionname and mission['getname'] == 'none':
                    mission['getname'] = account
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

    #%% mission complete
    def complete(self, account, missionname):
        
        complete_msg = 'mission complete'
        
        lock.acquire()
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            for mission in mission_data:
                if account == mission['getname'] and missionname == mission['missionname']:
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