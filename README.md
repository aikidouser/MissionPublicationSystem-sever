# Mission Publication System - Sever Side

- [ ] Socket
  - [x] handle msg
- [ ] Sign in
  - [x] Check the account and password correct
- [ ] Sign up 
  - [x] Set the user name
  - [x] Check if there are the same account
- [ ] Mission

# Account manage

## init 

```python
user = AccountManage(account, password)
```

## Sign up

```python
if_suc_signup = user.signup(username)
```

- 將回傳是否成功註冊
  - False
    - 已存在相同的帳號
  - True
    - 無相同帳號
    - 寫入json檔儲存

## Sign in

```python
if_suc_signin = user.signin()
```

- 回傳是否成功登入

  - False

    - 帳號 or 密碼有錯

    - 要求重新輸入

      > 重新建立新物件

  - True

    - 可繼續執行

# msg

## def msg handler

- return: 

  - dict
  - like the information above
  - ```msg_dict = msg_handler(str(msg))```

- arg: 

  - ```str(msg, encodeing='Big5')```


## Account
- information
    - account
    - password
    - username

- sign in
    - <font color=red> client -> sever</font>
    
       - ```python
          account signin 'account' 'password'
          ```
    
    - <font color = green>sever -> client</font>
    
      - if success
    
        - ```python
          account signin success 'username'
          ```
    
      - if fail
    
        - ```python
          account signin fail 
          ```
    
- sign up

    - <font color=red> client -> sever</font>

      - ```python
        account regist 'account' 'password' 'username'
        ```

    - <font color = green>sever -> client</font>

      - if success

        - ```python
          account regist success 'username'
          ```

      - if fail

        - ```python
          account regist fail
          ```

## Mission

- information
    - name

    - destination

    - deadline

    - salary

    - content

    - post

      > 發佈任務的人

    - get

      > 接取了任務的人，如果沒有設為空

    - complete

      > 是否完成

    - <font color=red> client -> sever</font>
    
        - ```python
            mission create 'missionname' 'destination' 'deadline' 'salary' 'content'
            ```
    
- read list
    - <font color=red> client -> sever</font>
    
        - ```python
            mission search all
            ```
    
    - <font color = green>sever -> client</font>
    
        - ```python
            mission search 'missionname' 'missionname' ......
            ```
    
- read the mission that client get
  
    - ```python
        mission search get
        ```
    
- read the mission that client post

    - ```python
        mission search post
        ```

- detail
  
    - <font color=red> client -> sever</font>
      
        ```python
        mission detail 'missionname'
        ```
    - <font color = green>sever -> client</font>
      
        ```python
        mission detail 'missionname' 'destination' 'deadline' 'salary' 'content'
        ```
    
- get
  
    - ```python
        mission get 'missionname'
        ```
    
    > - 比對 跟任務不同的 account 才可以 get
    >
    > - get 後再次回傳
    
- complete
  
    - ```python
        mission complete 'missionname'
        ```
    
    > 比對 跟任務相同的 account 才可以 complete

