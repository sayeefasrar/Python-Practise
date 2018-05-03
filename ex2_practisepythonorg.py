"""Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.

Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number
to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message."""

num=input("Enter a number: ")

if (num%2)==0 :
    if (num%4)==0:
        print ("Mutiple of 4")
    else:
        print("Number provided is even")
    
elif (num%2)==1:
    print ("Number provided is odd")

