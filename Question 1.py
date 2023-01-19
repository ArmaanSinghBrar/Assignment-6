#Finding if an integer is a perfect integer
num = int(input("Enter an integer :"))
Sum_of_factors=0
for i in range(1,num):                 #Running a loop for all numbers in range 1 to num
    if num%i==0:                       #Finding if the number is a factor of the integer
        Sum_of_factors+=i              #If a factor add it to the sum of factors
if Sum_of_factors==num:                #If condition is satisfied it is a perfect integer
    print(num,"is a perfect integer")
else:
    print(num,"is not a perfect integer")
