---
title: Mission Pub Sys_Server
tags: 1092, Python
---

# Mission Publication System

# msg

## Account
- information
    - account
    - password
    - username

- sign in
    - client -> server
        ```python=
        account signin 'account' 'password'
        ```
    - server -> client
        ```python=
        account signin success 'username'
        ```
        ```python=
        account signin fail
        ```

- sign up
    -  client -> server
        ```python=
        account regist 'account' 'password' 'username'
        ```
    - server -> client
        ```python=
        account regist success/fail
        ```

## Mission

- information
    - name
    - destination
    - deadline
    - salary
    - content

- create
    - client -> sever
        ```python=
        mission create 'missionname' 'destination' 'deadline' 'salary' 'content'
        ```
    - sever -> client
        ```python=
        mission create success 'missionname'
        ```

- search
    - client -> sever
        ```python=
        mission search all
        ```
        ```python=
        mission search get
        ```
        ```python=
        mission search post
        ```
    - sever -> client
        ```python=
        mission search 'missionname' 'missionname' ......
        ```
        > json未建立 或 無此任務
        ```python=
        mission search 
        ```
- search keyword
    - client -> sever
        ```python=
        mission search keyword missionname|destination|content 'target'
        ```
    - sever -> client
        ```python=
        mission search keyword missionname|destination|content 'result1' 'result2' ......
        ```
        > json未建立 或 無此結果
        ```python=
        mission search keyword missionname|destination|content
        ```
- detail
    - client -> sever
        ```python=
        mission detail 'missionname'
        ```
    - sever -> client
        - 此帳號是否可評價此任務的接取者
            ```python=
            mission detail scorable/nonscorable 'postname' 'missionname' 'destination' 'deadline' 'salary' 'content'  
            ```
            > - 帳號需相同於post account
            > - 任務需完成
    - json未建立 或 無此任務
        ```python=
        mission detail fail
        ```
        > 應不會發生
- score
    - client -> sever
        ```python=
        mission score 'missionname' 1/-1
        ```
    - sever -> client
        ```python=
        mission score success/fail
        ```
- get
    - client -> sever
        ```python=
        mission get 'missionname'
        ```
    - sever -> client
        > 比對 跟任務不同的 account 才可以 get
        ```python=
        mission get success 'missionname'
        ```
        > json未建立 或 跟任務相同account 或 無此任務
        ```python=
        mission get fail
        ```

- complete
    - client -> sever
        ```python=
        mission complete 'missionname'
        ```
    - sever -> client
        > 比對 跟任務相同的 account 才可以 complete
        ```python=
        mission complete 'missionname'
        ```
## def msg_handler

- returen: 
    - dict
    - like the information above

- arg: 
    - str(msg, encodeing='Big5')

    ```python=
    msg_dict = msg_handler(str(msg))
    ```
