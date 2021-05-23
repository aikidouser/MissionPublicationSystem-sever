# Mission Publication System - Sever Side

- [ ] Socket
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

