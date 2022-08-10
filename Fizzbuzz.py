num=int(input("Enter the number of terms for the Fizz_buzz: "))
for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0: 
        print("Fizz_Buzz") 
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    else:
        print(i)