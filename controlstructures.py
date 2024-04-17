"""
->Control Structures!
 Control structures are fundamental concepts in programming
 that dictate the flow of execution based on certain conditions or criteria.
 part's of Control Structures
 (1) Conditional Statements:  This make a decision based on conditions.
    Ex ->
     if statement
     else statement
     switch statement
 (2) Loops: Loops are used to execute a block of code repeatedly.
            They continue to execute until a certain condition is met.
        Ex->
            for loops
            while loops
            do-while loops
 (3) Jump Statements: These statements change the normal flow of control by transferring program control to another
                      part of the code .
                    Ex ->
                      Brake
                      continue
                      return
"""

#  code on Conditional Statements
# Use if statements to execute a block of code if a specified condition is true.
# Use else statements to execute a block of code if the same condition is false.
# Use else if statements to specify a new condition if the first condition is false.

x = 10
if x > 5:
    print("X is greater than 5")
elif x == 5:
    print("X is equal to 5")
else:
    print("X is less than 5")

# code in LOOPS
# for loops is to iterate over a sequence (such as list or range of number )a specific number of time.
# while loops is to execute a bloke of code repeatedly as long as a specified condition is true.
# CODE
# this is for loop

for i in range(5):
    print(i)
    # This will print a 0 to 4 number .because in computer take value form 0 and onward.
print("The range() function returns a sequence of numbers, starting from 0 by default,and"
      " increments by 1(by default),"" and stops before a specified number. ")
# Using while loops
x = 0
while x < 5:
    print(x)
    x += 1
# This will print a 0 to 4 number.
print("the Jump statement ")
# Using break
for i in range(10):
    if i == 5:
        break
    print(i)
# break to exit a loop prematurely.
# Using continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# continue to skip the rest of the current iteration of a loop and continue with the next iteration.
# Using return
def add(x, y):
    return x + y
# return to exit a function and optionally return a value.


# This is 5 project on this to build  knowledge
"""
(1)
Simple Calculator: Create a program that acts as a basic calculator. It should take input from the user for two numbers 
and an operation (addition, subtraction, multiplication, division) and then perform the operation using conditional 
statements.
(2)
Number Guessing Game: Develop a game where the computer generates a random number and the player has to guess it. Use 
loops to allow the player to keep guessing until they guess correctly. Provide feedback to the player if their guess is
too high or too low.
(3)
Temperature Converter: Build a program that converts temperatures between Celsius and Fahrenheit. Allow the user to 
choose the conversion direction and input the temperature. Use conditional statements to perform the conversion.
(4)
To-Do List Manager: Create a simple to-do list manager where users can add, remove, and view tasks. Use loops to 
repeatedly display the menu and prompt the user for actions until they choose to exit.
(5)
Simple Quiz Game: Develop a quiz game with multiple-choice questions. Use conditional statements to check if the user's 
answer is correct and keep track of their score.
"""
