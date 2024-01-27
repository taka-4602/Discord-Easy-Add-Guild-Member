import requests

headers = {"Content-Type": "application/x-www-form-urlencoded"}

class EGAM:
    def __init__(self,bot_token:str=None,client_id:str=None,client_secret:str=None,redirect_uri:str=None,proxy:dict=None):
        self.proxy=proxy
        self.bot_token=bot_token
        self.data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri
        }    

    def get_token(self,code:str) -> dict:
        data=self.data
        data["grant_type"]="authorization_code"
        data["code"]=code
        gettoken = requests.post("https://discord.com/api/v10/oauth2/token", data=data, headers=headers,proxies=self.proxy)
        return gettoken.json()
    
    def get_user(self,access_token:str) -> dict:
        user = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f"Bearer {access_token}"},proxies=self.proxy)
        return user.json()

    def refresh(self,refresh_token:str):
        data=self.data
        data["grant_type"]="refresh_token"
        data["refresh_token"]=refresh_token
        refresh=requests.post("https://discord.com/api/v10/oauth2/token", data=data, headers=headers,proxies=self.proxy)
        if not refresh.status_code < 300:
            return refresh.status_code
        return refresh.json()

    def add_member(self,access_token:str,user_id:str,guild_id:str):
        head = {"Authorization": "Bot " + self.bot_token, "Content-Type": "application/json"}
        adgm=requests.put("https://discord.com/api/guilds/" + guild_id + "/members/" + user_id, headers=head, json={"access_token": access_token},proxies=self.proxy)
        return adgm.status_code
    
    def add_role(self,user_id:str,guild_id:str,role_id:str):
        head = {"Authorization": "Bot " + self.bot_token, "Content-Type": "application/json"}
        role=requests.put("https://discord.com/api/guilds/" + guild_id + "/members/" + user_id + "/roles/" + role_id, headers=head)
        return role.status_code