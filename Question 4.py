#Function to check if a string is a pangram
def pangram(string):
    string=string.lower()
    for i in range(97,123):        #running a loop for all alphabets
        statement=chr(i) in string   #Statement is true or false
        if statement==False:         #If statement becomes false at any point the string is not a pangram
            return False
    else:
        return True

print(pangram("The quick brown fox jumps over the lazy dog"))   #An Example
