person = input("Enter a name ")
age = input("Enter the age ")
thing= input("Enter a thing ")
good= input("Enter the personality ")
person2 = input("Enter a name")
Gender= input("Enter your gender (male/female): ").strip().lower()
if Gender == "male":
    print("You are male ")
elif Gender == "female":
    print("You are female")
else:
    print("Invalid input. Please enter 'male' or 'female'. ")    

print("This is " + person)
print("This person is " +  age + " year old")
print("This person has a " + thing)
print( person + " personality is " + good)
print( person + " girlfriend is " + person2)