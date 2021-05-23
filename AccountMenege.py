#%%
import json

#%%
class AccountMenege:
    
    def __init__(self, account, password):  
        
        self.account = account
        self.password = password
        
    #%% Record the new user
    def signup(self, username):
        
        user_dict = {'username' : username,
                     'account' : self.account,
                     'password' : self.password}
        
        try:
            with open ('test_json.json', 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            data = list()
            
        if_same = self.check_if_same(data)
        if(if_same):
            return False    #There are the same account
        
        with open('test_json.json', 'w', ) as json_file:
            data.append(user_dict)
            json.dump(data, json_file)
        
        return True     #Success signup
    
    #%%
    def signin(self):
        
        with open('test_json.json', 'r') as json_file:
            user_data = json.load(json_file)
            
        for user in user_data:
            if(self.account == user['account'] and self.password == user['password']):
                return True
            
        return False
            
    #%%
    def check_if_same(self, data):
        
        for user in data:
            if(self.account == user['account']):
                return True
            
        return False
    