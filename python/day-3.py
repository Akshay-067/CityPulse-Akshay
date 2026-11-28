print("Hello World")

# variables
name="Aarav"
age=19
attendance=92.5
is_present=True
print(name)
print(type(age))
print(type(attendance))
print(type(is_present))


# input 
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hi {name}, you are {age} years old.")


# f-strings
city = "Bangalore"
temp = 22.5
print(f"The temperature in {city} today is {temp}°C.")
print("The temperature in",{city},"today is",{temp},"°C.")

number=int("5")
float=float("3.14")
string=str(100)

print(number)
print(float)
print(string)

four= 1000
two = 37


print(four + two)   
print(four - two)   
print(four * two)   
print(four / two)   
print(four // two)   
print(four % two)   
print(four ** two)   


marks = 67
passed = marks >= 33
good_score = marks >= 80

print(passed)                      
print(good_score)                 
print(passed and good_score)   

bonus = 10
marks += bonus
print(f"Marks after bonus: {marks}")



Age = int(input("Enter Age: "))

if Age >= 90:
    print("Too OLD")
elif Age >= 75:
    print("OLD")
elif Age >= 40:
    print("Almost OLD")
elif Age <=30:
    print("Young")
else:
    print("Try again")


# height1 = int(input("Enter first number: "))
# height2= int(input("Enter second number: "))

# if height1 > height2:
#     print(f"{height1} is taller")
# elif height2 > height1:
#     print(f"{height2} is taller")
# else:
#     print("Both are equal")


fruits = ["apple", "banana", "mango"]
print(fruits.index("mango")) 


subjects={"":{"":"","":"","":""},
          "":{"":"","":"","":""},
          "":{"":"","":"","":""}}