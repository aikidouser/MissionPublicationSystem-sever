#%%
from AccountMenege import AccountMenege

#%%
if __name__ == "__main__":
    
    while(True):
        creat_ac = int(input('signup?: '))
        account = input('account: ')            #Get account
        password = input('password: ')          #Get password
        user = AccountMenege(account, password) 
        
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
                    

# =============================================================================
# with open ('test_json.json', 'r') as jsonfile:
#     
#     data = json.load(jsonfile)
# =============================================================================
