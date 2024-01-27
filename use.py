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