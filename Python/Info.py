name =input("Enter your name") 
age =input("Enter your age")
def sayhi(name , age):
    print("Welcome " + name)
    print("You are " + age + " year old ")

sayhi(name , age)
# Function to add two numbers
def add (x , y):
    return x + y

#Function to sub two numbers
def sub(x , y):
    return x - y

#Function to multiply two numbers
def multiply(x , y):
    return x * y

#Function to divide two numbers
def divide(x , y):
    return x / y

x =float(input("Enter a number: "))
y =float(input("Enter a number: "))

result1 = add(x, y)
result2 = sub(x, y)
result3 = multiply(x, y)
result4 = divide(x , y)

print(f"The result of adding {x} and {y} is: {result1}")
print(f"The result of subtracting {x} and {y} is: {result2}")
print(f"The result of multiplying {x} and {y} is: {result3}")
print(f"The result of divide {x} and {y} is: {result4}")