class Comment:
  def __init__(self, username, text, likes = 0):
    self._username = username
    self._text = text
    self._likes = likes

c = Comment("davey123", "lol you're so silly", 3) 
print(c._username)    #"davey123"
print(c._text)           #"lol you're so silly"
print(c._likes)          #3
another_comment = Comment("rosa77", "soooo cute!!!") 
print(another_comment._username)       #"rosa77"
print(another_comment._text)            #"soooo cute!!!"
print(another_comment._likes)           #0 