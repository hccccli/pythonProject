import itchat

def find_friend(nick_name):
  for friend in itchat.get_friends():
    if friend['NickName'] == nick_name:
      return friend

def main():
  itchat.auto_login(True)
  friend = find_friend('spiritual')
  username = friend['UserName']
  itchat.send(msg='你好啊',toUserName=username)
  itchat.logout()

if __name__ == "__main__":
  main()