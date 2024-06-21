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