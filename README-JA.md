# Discord-Easy-Add-Guild-Member
Discordのメンバー追加API、Add Guild MemberのシンプルなAPIラッパー  
バックアップBot、メン爆Bot などに使えます  
### >> ```pip install EAGM``` <<
### このAPIラッパーを使用したバックアップBotを公開してます！
https://github.com/taka-4602/Discord-Backup-Bot
## 使ってみる (超シンプル！)
#### example.py
```python
from EAGM import EAGM

token="Discord Botのトークン"
cid="クライアントID"
cse="クライアントシークレット"
ruri="リダイレクト先"

eagm=EGAM(bot_token=token,client_id=cid,client_secret=cse,redirect_uri=ruri,proxy=None)#proxyにプロキシを設定できます (proxy=dict)

eagm.get_token("code")#アクセストークン、リフレッシュトークンを取得する
print(eagm.access_token)
print(eagm.refresh_token)
eagm.get_user(eagm.access_token)#トークンからユーザー情報を取得 (ユーザーID / ユーザーネーム など)
print(eagm.user_id)
print(eagm.username)
print(eagm.avatar)
print(eagm.add_role(user_id="1234567890",guild_id="1234567890",role_id="1234567890"))#ユーザーにロールを付与
print(eagm.add_member(access_token="access_token",user_id="1234567890",guild_id="1234567890"))#ユーザーをサーバーに追加
eagm.refresh("refresh_token")#リフレッシュトークンでトークンをリフレッシュする
print(eagm.refreshed_access_token)
print(eagm.refreshed_refresh_token)
```
#コメントで書いてあることがすべてです、これがバックアップBotのコアのすべてということです  
### もう少し知る
```EAGM.get_token```  
- 成功、失敗に関わらずdictが返されます  
  トークン、アクセストークン、有効期限がわかります  

```EAGM.get_user```
- dictでユーザー情報がたくさん知れます  
  ```
  {'id': '614025927877197834', 'username': '.taka.', 'avatar': '8057538b821aad2e5995cdaf5d94c173', 'discriminator': '0', 'public_flags': 4194560, 'premium_type': 2, 'flags': 4194560, 'banner': '05f76c61f15f5c073ef53c14c2528ff8', 'accent_color': 65573,
  'global_name': 'たか', 'avatar_decoration_data': {'asset': 'a_d3da36040163ee0f9176dfe7ced45cdc', 'sku_id': '1144058522808614923'}, 'banner_color': '#010025', 'mfa_enabled': False, 'locale': 'en-US'}
  ```
  
```EAGM.add_role```
- HTTPのステータスコードがintで返されます  
  ```204```以外は失敗です

```EAGM.add_member```
- add_roleと同じくステータスコードがintで返されます  
  ```201``` / 成功  
  ```204``` / 追加する前から既にサーバーにいる  
  ```403``` / アクセストークンが無効  
  ```400``` / 追加するユーザーのサーバー参加上限

```EAGM.refresh```
- 成功するとdict、失敗するとステータスコードがintで返されます  
  ```400``` / ユーザーがアプリケーション認証を切っている  
## コンタクト
サーバー / https://discord.gg/aSyaAK7Ktm  
Discord / .taka.  
