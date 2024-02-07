from EAGM import EAGM

token="Discord Bot Token"
cid="Client ID"
cse="Client Secret"
ruri="Redirect URI"

eagm=EAGM(bot_token=token,client_id=cid,client_secret=cse,redirect_uri=ruri,proxy=None)#you can set any proxy (proxy=dict)

print(eagm.get_token("code"))#get any tokens
print(eagm.get_user("access_token"))#get user infomation (like user id / user name)
print(eagm.add_role(user_id="1234567890",guild_id="1234567890",role_id="1234567890"))#add role to user
print(eagm.add_member(access_token="access_token",user_id="1234567890",guild_id="1234567890"))#add user to guild
print(eagm.refresh("refresh_token"))#refresh OAuth2 AccessToken