print("Hello World")
import sys
print(sys.version)

a = input("Ente a number: ")
c = input("Enter a number: ")
if (a > c):
    print(a + " is greater than " + c )
elif (a == c):
    print(a + " is equall to " + c)
else:
    print(a + " is smaller than " + c)

set = ["Lion", "Tiger", "Cat"]
for Animal in range(5):
    if Animal == 2:
        print("first Iteration")
    else:
        print("Not first")