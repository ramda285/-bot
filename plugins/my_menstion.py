from slackbot.bot import respond_to # @botname: で反応するデコーダ
from slackbot.bot import listen_to # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply # 該当する応答がない場合に反応するデコーダ
import random

@respond_to(':hand:')
def mention_func(message):
  x = random.randint(1,100)
  if x != 1:
    pon = ":V:"
    janken(message, pon)
  else:
    pon = ":fist:"
    win(message, pon)
  
@respond_to(':fist:')
def mention_func(message):
  x = random.randint(1,100)
  if x != 1:
    pon = ":hand:"
    janken(message, pon)
  else:
    pon = ":V:"
    win(message, pon)

@respond_to(':V:')
def mention_func(message):
  x = random.randint(1,100)
  if x != 1:
    pon = ":fist:"
    janken(message, pon)
  else:
    pon = ":hand:"
    win(message, pon)

@respond_to(':fu:')
def mention_func(message):
  message.send('じゃんけんポン！:punch: :neutral_face:\nYOU DIED')

def janken(message, pon):
  y = random.randint(1,18)
  message.send('じゃんけんポン！' + pon + ':neutral_face:\n\nYOU LOSE(ﾌﾞｳｳｳｳｳｳ!!!!)\n\n俺の勝ち！:grin:\n')
  if y == 1:
    message.send('なんで負けたか、明日まで\n考えといてください。\nそしたら何かが\n見えてくるはずです。\n')
  elif y == 2:
    message.send('たかがじゃんけん、そう思ってないですか？\nそれやったら明日も\n俺が勝ちますよ。\n')
  elif y == 3:
    message.send('負けは次につながる\nチャンスです。\nネバーギブアップ！\n')
  elif y == 4:
    message.send('ただの運やと思ってませんか？\n運も実力のうち！聞いたことありますよね？\n')
  elif y == 5:
    message.send('複雑に考えてないですか？\n答えはシンプルです\nケイスケ　ホンダの心を読む\nそれだけです\n')
  elif y == 6:
    message.send('自信を持って\n勝負にしっかりと向き合える\nそう思えるまで、準備してください\n')
  elif y == 7:
    message.send('ウラのウラのウラまで\n読む訓練をしておいてくださいね\nどこまで読もうとするかで\n結果が変わってきます\n')
  elif y == 8:
    message.send('どんな事でも\n絶対に勝つんや！という\nメンタリティーが大事ですよ\n')
  elif y == 9:
    message.send('いい勝負でしたね！\nでも\n結果が伴わないと全く意味がありません\n')
  elif y == 10:
    message.send('ちゃんと分析してます？\nじっくり結果に向き合ってください\n')
  elif y == 11:
    message.send('運を味方につけるのは\n地道な努力ですよ\n')
  elif y == 12:
    message.send('動揺してませんか？\n運が大事な時こそ\n集中力が物を言いますよ！\n')
  elif y == 13:
    message.send('何事も準備がすべて\nそれを怠っていることが\nバレてますよ\n')
  elif y == 14:
    message.send('ここは練習では\nありません\n全身全霊で\n俺と向き合ってください\n')
  elif y == 15:
    message.send('あなたの考えていることぐらい\n俺にはお見通しです\n')
  elif y == 16:
    message.send('その程度の、\n気持ちで勝てるとでも\n思ったんですか？\nちゃんと練習してきてください\n')
  elif y == 17:
    message.send('それで勝てると\n思ってるんやったら\n俺がずっと勝ちますよ！\n')
  elif y == 18:
    message.send('1年間\n何やってたんですか？\nこの結果は\nじゃんけんに対する\n意識の差です\n')
  message.send('ほな、いただきまーす(ﾌﾞｼｭｳｳｳｳｳｳｳ)\n\nうまい！:yum:\n一日一回勝負。じゃあ、また明日:wave::blush:')

def win(message, pon):
  message.send('じゃんけんポン！' + pon +'やるやん！:hushed:\n明日は俺にリベンジさせて。\nでは、どうぞ。\nつhttp://urx.space/mCWU')
  
@default_reply()
def default_func(message):
    message.reply('新発売になった\nこのペプシ ジャパンコーラ\n飲んでみたくないですか？:smirk:\n僕と勝負して勝ったら、\n一本あげますよ\n\nじゃーんけん')