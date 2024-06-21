# Discord-Easy-Add-Guild-Member
A simple API wrapper for Discord Add Guild Member  
For Member-Boost Bot, Member-Backup Bot ( Yes, it's same as RestoreCord )  
### >> ```pip install EAGM``` <<
### 日本語はこちら -> [README-JA](https://github.com/taka-4602/Discord-Easy-Guild-Add-Member/blob/main/README-JA.md)
## Try using it ! ( It's too simple, But it does any good jobs ! )
#### example.py
```python
from EAGM import EAGM

token="Discord Bot Token"
cid="Client ID"
cse="Client Secret"
ruri="Redirect URI"

eagm=EAGM(bot_token=token,client_id=cid,client_secret=cse,redirect_uri=ruri,proxy=None)#you can set any proxy (proxy=dict)

eagm.get_token("code")#get any tokens
print(eagm.access_token)
print(eagm.refresh_token)
eagm.get_user(eagm.access_token)#get user infomation (like user id / user name)
print(eagm.user_id)
print(eagm.username)
print(eagm.avatar)
print(eagm.add_role(user_id="1234567890",guild_id="1234567890",role_id="1234567890"))#add role to user
print(eagm.add_member(access_token="access_token",user_id="1234567890",guild_id="1234567890"))#add user to guild
eagm.refresh("refresh_token")#refresh OAuth2 AccessToken
print(eagm.refreshed_access_token)
print(eagm.refreshed_refresh_token)
```
I wrote how to use it in the #comments, And it's all  
Incorporate this code into your Member-Backup Bot!   
### Know a little more
```EAGM.get_token```  
- A dict is returned regardless of success or failure  
  You can get access token, refresh token, and expiration date  

```EAGM.get_user```
- It's return a dict, and you can find out a lot of user information with this  
  ```
  {'id': '614025927877197834', 'username': '.taka.', 'avatar': '8057538b821aad2e5995cdaf5d94c173', 'discriminator': '0', 'public_flags': 4194560, 'premium_type': 2, 'flags': 4194560, 'banner': '05f76c61f15f5c073ef53c14c2528ff8', 'accent_color': 65573,
  'global_name': 'たか', 'avatar_decoration_data': {'asset': 'a_d3da36040163ee0f9176dfe7ced45cdc', 'sku_id': '1144058522808614923'}, 'banner_color': '#010025', 'mfa_enabled': False, 'locale': 'en-US'}
  ```
  
```EAGM.add_role```
- HTTP response status codes is returned as an int  
  ```204``` is success, other is failing

```EAGM.add_member```
- HTTP response status codes is returned as an int, same as add_role  
  ```201``` / Success  
  ```204``` / User is already on that server   
  ```403``` / Access token is invalid  
  ```400``` / User's server limit

```EAGM.refresh```
- Returns dict on success, status code in int on failure  
  ```400``` / User was deauthorized your app  
### Example Bot is here -> [Discord-Backup-Bot](https://github.com/taka-4602/Discord-Backup-Bot)
#### ( Sorry for not using English )
