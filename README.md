# Discord-Easy-Guild-Add-Member
A simple API wrapper for Discord Guild Add Member  
For Member-Boost Bot, Member-Backup Bot ( Yes, it's same as RestoreCord )  
### 日本語はこちら -> [README-JA](https://github.com/taka-4602/Discord-Easy-Guild-Add-Member/blob/main/README-JA.md)
## Try using it ! ( It's too simple, But it's does any good jobs ! )
#### use.py
```python
from EGAM import EGAM

token="Discord Bot Token"
cid="Client ID"
cse="Client Secret"
ruri="Redirect URI"

egam=EGAM(bot_token=token,client_id=cid,client_secret=cse,redirect_uri=ruri,proxy=None)#you can set any proxy (proxy=dict)

print(egam.get_token("code"))#get any tokens
print(egam.get_user("access_token"))#get user infomation (like user id / user name)
print(egam.add_role(user_id="1234567890",guild_id="1234567890",role_id="1234567890"))#add role to user
print(egam.add_member(access_token="access_token",user_id="1234567890",guild_id="1234567890"))#add user to guild
print(egam.refresh("refresh_token"))#refresh OAuth2 AccessToken
```
I wrote how to use it in the #comments, And it's all  
Incorporate this code into your Member-Backup Bot!   
### Know a little more
```EGAM.get_token```  
- A dict is returned regardless of success or failure  
  You can see the token, access token, and expiration date  

```EGAM.get_user```
- It's return a dict, and you can find out a lot of user information with this  
  ```
  {'id': '614025927877197834', 'username': '.taka.', 'avatar': '8057538b821aad2e5995cdaf5d94c173', 'discriminator': '0', 'public_flags': 4194560, 'premium_type': 2, 'flags': 4194560, 'banner': '05f76c61f15f5c073ef53c14c2528ff8', 'accent_color': 65573,
  'global_name': 'たか', 'avatar_decoration_data': {'asset': 'a_d3da36040163ee0f9176dfe7ced45cdc', 'sku_id': '1144058522808614923'}, 'banner_color': '#010025', 'mfa_enabled': False, 'locale': 'en-US'}
  ```
  
```EGAM.add_role```
- HTTP response status codes is returned as an int  
  Status ```204``` is looks like success, but it's failing

```EGAM.add_member```
- HTTP response status codes is returned as an int, same as add_role  
  ```201``` / Success  
  ```204``` / User is already on that server   
  ```403``` / Access token is invalid  
  ```400``` / User's server limit

```EGAM.refresh```
- Returns dict on success, status code in int on failure  
  ```400``` / User was deauthorized your app  
