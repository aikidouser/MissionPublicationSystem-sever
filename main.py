#%%
import json
from AccountMenege import AccountMenege

#%%
if __name__ == "__main__":
    
    for i in range(0, 2):
        creat_ac = input('input: ')
        account = input('account: ')
        password = input('password: ')
        username = input('username: ')
        
        user = AccountMenege(account, password)
        
        if_success = user.signup(username)
        
        if(if_success):
            print('You did it')
        else:
            print('rrrrr')

#%%
with open ('test_json.json', 'r') as jsonfile:
    
    data = json.load(jsonfile)