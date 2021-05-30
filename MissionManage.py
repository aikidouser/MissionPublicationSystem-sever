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
    def create(self, missionname, destination, deadline, salary, content, postname):

        self.missionname = missionname
        self.destination = destination
        self.deadline = deadline
        self.salary = salary
        self.content = content
        self.postname = postname
        self.getname = 'none'

        mission_dict = {'missionname' : self.missionname,
                        'destination' : self.destination,
                        'deadline' : self.deadline,
                        'salary' : self.salary,
                        'content' : self.content,
                        'postname' : self.postname,
                        'getname' : self.getname}
        
        lock.acquire()
        try:
            with open ('mission_info.json', 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            data = list()

        with open('mission_info.json', 'w') as json_file:
            data.append(mission_dict)
            json.dump(data, json_file)
            
        lock.release()

        return True     #mission create Success


    #%% mission search
    def search(self, username, agp):
        
        self.missionsearch = ''
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
                
            if agp == 'all':
                for mission in mission_data:
                    self.missionsearch += (' ' + mission['missionname'])
            elif agp == 'get':
                for mission in mission_data:
                    if username == mission['getname']:
                        self.missionsearch += (' ' + mission['missionname'])
            elif agp == 'post':
                for mission in mission_data:
                    if username == mission['postname']:
                        self.missionsearch += (' ' + mission['missionname'])

        except Exception:    
            return False
        
        return True

    #%% mission detail
    def detail(self, missionname):
        
        self.missiondetail = ''
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
            for mission in mission_data:
                if missionname == mission['missionname']:
                    self.missiondetail = ' ' + mission['missionname'] + ' ' + mission['destination'] + ' ' + mission['deadline'] + ' ' + mission['salary'] + ' ' + mission['content']
                    break

        except Exception:    
            return False
        
        return True

    #%% mission get
    def get(self, username, missionname):
        
        if_sus_get = False
        
        lock.acquire()
 
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
            for mission in mission_data:
                if username != mission['postname'] and missionname == mission['missionname']:
                    mission['getname'] = username
                    if_sus_get = True
                    break

        except Exception:    
            lock.release()
            return False
        
        with open('mission_info.json', 'w') as json_file:
            json.dump(mission_data, json_file)

        lock.release()
        
        if if_sus_get:
            return True
        elif if_sus_get:
            return False

    #%% mission complete
    def cmoplete(self, username, missionname):
        
        if_sus_complete = False
        
        lock.acquire()
 
        try:
            with open('mission_info.json', 'r') as json_file:
                mission_data = json.load(json_file)
            for mission in mission_data:
                if username == mission['getname'] and missionname == mission['missionname']:
                    mission_data.remove(mission)
                    if_sus_complete = True
                    break

        except Exception:    
            lock.release()
            return False
        
        with open('mission_info.json', 'w') as json_file:
            json.dump(mission_data, json_file)

        lock.release()
        
        if if_sus_complete:
            return True
        elif if_sus_complete:
            return False
