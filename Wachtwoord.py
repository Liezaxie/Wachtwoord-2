import re
x = 1 #zorgt voor de loop en laat je falen als je het te vaak verkeerd doet.
S = 0 #sterkte van het wachtwoord.
while x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
  print("Password needs: At least 8 characters."
        " 1 of these symbols: $#@!%^&*:;."
        " 1 Uppercase letter."
        " 1 Lowecase letter. ")
  W = input("Input your password:")
  if (len(W)<8):
    print("To short!")
    x = x+1
  elif not re.search("[a-z]",W):
      print("No lowercase in password!")
      x = x+1
  elif not re.search("[0-9]",W):
      print("No numbers in password!")
      x = x+1
  elif not re.search("[A-Z]",W):
      print("No uppercase in password!")
      x = x+1
  elif not re.search("[$#@!%^&*:;]",W):
      print ("No special characters in password!")
      x = x+1
  else:
    print("good")
    x = 0
#if re.search("[a-z]",W) >=1:
#    S = S+1
#    if re.search("[0-9]",W):

if x == 0:
    print()
if x == 6:
    print("You are a idiot sandwich!!")
