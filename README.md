# 本田とじゃんけん
![本田圭佑](https://i.imgur.com/73OAw7E.jpg)

本田に1年間何やってたんだ見たいなこと言われたから、  
来年のじゃんけんに向けて特訓したい人向け
### 使い方：
slack apiでlegacyバージョン(rmt:streamが使える奴)のアプリケーションを作成して、  
出力されたtokenをslackbot_settings.pyのAPI_TOKEN = "xoxb-xxxxxxx..."の中に入れる。  
その後run.pyを起動する。
### バージョン：1.0  
### 使用ライブラリ：lins05/slackbot  
### 今後に追加したい仕様  ：
`@default_reply()` にてじゃんけんの選択肢を表示して、  
ボタンをクリックすることでじゃんけんできるようにしたい。  