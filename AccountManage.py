#%%
import json
import threading

#%%
lock = threading.Lock()

#%%
class AccountManage:
    
    def __init__(self, account, password):  
        
        self.account = account
        self.password = password
        
    #%% Record the new user
    def signup(self, username):
        
        self.username = username
        user_dict = {'username' : self.username,
                     'account' : self.account,
                     'password' : self.password}
        
        lock.acquire()
        try:
            with open ('user_info.json', 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            data = list()
            
        if_same = self.check_if_same(data)
        if(if_same):
            lock.release()
            return False    #There are the same account
        
        with open('user_info.json', 'w', ) as json_file:
            data.append(user_dict)
            json.dump(data, json_file)
            
        lock.release()

        
        return True     #Success signup
    
    #%%
    def signin(self):
        
        try:
            with open('user_info.json', 'r') as json_file:
                user_data = json.load(json_file)
                
            for user in user_data:
                if(self.account == user['account'] and self.password == user['password']):
                    self.username = user['username']
                    return True

        except Exception:    
            pass
        
        return False
            
    #%%
    def check_if_same(self, data):
        
        for user in data:
            if(self.account == user['account']):
                return True
            
        return False
    
#%%
if __name__ == "__main__":
    
    while(True):
        creat_ac = int(input('signup?: '))
        account = input('account: ')            #Get account
        password = input('password: ')          #Get password
        user = AccountManage(account, password) 
        
        if(creat_ac):

            username = input('username: ')
            
            if_suc_signup = user.signup(username)
            
            if(if_suc_signup):
                print('You did it')             #return signup success
            else:
                print('rrrrr')                  #return signup fail
        
        else:
            if_suc_signin = user.signin()
            
            if(if_suc_signin):
                print('Wellcome')               #return signin success
            else:
                print('Wrong')                  #return signin fail