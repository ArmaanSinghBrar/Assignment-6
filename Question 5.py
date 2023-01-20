#printing words separated by hyphens after sorting them alphabetically
List=input("Enter words separated by a hyphen :").split("-")  #Turning string into a list separated by hyphen
List.sort()               #Sorting the list
print("-".join(List))     #printing the list joined by hyphens
