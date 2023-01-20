#Finding if a string is palindrome
def palindrome(string):
  String=string.replace(" ","")
  reversed_string=String[::-1]             #Reversing the string
  if String==reversed_string:              #If string stays same when reversed it is a palindrome
    return True
  else:
    return False
