#Finding if a string is palindrome
String=input("Enter a string :")
Reversed_String=String[::-1]             #Reversing the string
if String==Reversed_String:              #If string stays same when reversed it is a palindrome
    print(String,"is a palindrome")
else:
    print(String,"is not a palindrome")
