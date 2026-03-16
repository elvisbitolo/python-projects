#Exercise 1
print(("Hello world\n")*4)
#Exercise 2
print((99^3)*8)
#Exercise 3
15 < 8                 #false
5 > 3                  #true
3 == 3                 #true
3 == "3"               #false
"3" > 3                 #error
"Hello" == "hello"     #false

#Exercise 4
computer_brand = "lenovo"
print(f"I have a {computer_brand} computer.")

#Exercise 5
name = "elvis bitolo"
age = 27
shoe_size = 42
info=f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

#Exercise 6
a = 5
b = 1
if a > b:
    print("Hello World")
#Exercise 7
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#Exercise 8
name = input("Enter your name: ")
if name == "elvis bitolo":
    print(f"wow {name}, i am also called {name}")
else:
    print(f"Hello {name}, nice to meet you!")
#Exercise 9
height = float(input("Enter your height in cm: "))
if height > 145:    
    print("You are tall enough to ride the roller coaster.")
else:
    print("Grow some more to ride the roller coaster.")