import random
#imports random module form python databse for further useage in the code

guessesTaken = 0
#declars a variable and assignss its value to 0

print('Hello! What is your name?')
#the string in the brackets will be displayed on the screen upon execution
myName = input()
#declares a variable and assigns it to a user input

number = random.randint(1, 20)
#declares a variable and assigns it to a random intiger between 1 and 20 using the random module imported before
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
#the string in the brackets will be displayed upon executions including a variable

while guessesTaken < 6:
    #introducing a while loop so intill the variable is less then 6 the loop will run
    print('Take a guess.')
    #the string in the brackets will be displayed on the screen upon execution
    guess = input()
    #declares jet again a variable and assigns it to user input
    guess = int(guess)
    #converts the before declared input into an intiger

    guessesTaken += 1
    #assigns the variable to be itself but incresed by 1

    if guess < number:
        #introduces a conditional statement that the first variable has to be less than the other
        print('Your guess is too low.')
        #if the above condition returns True, the a the string in the bracets will be displayed

    if guess > number:
        #introduces a conditional statement that the first variable has to be higher than the other
        print('Your guess is too high.')
        #if the above condition returns True, the a the string in the bracets will be displayed

    if guess == number:
        #introduces a conditional statement that the first variable is equal the other
        break
        #if the above condition returns True, the loop will stop

if guess == number:
    #introduces a conditional statement that the first variable is equal the other
    guessesTaken = str(guessesTaken)
    #converts the variable declared before into an intiger

    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    #if the above condition returns True, the a the string in the bracets will be displayed, including the variables

if guess != number:
    #introduces a conditional statement that the first variable is not equal the other
    number = str(number)
    #converts the variable declared before into an intiger
    print('Nope. The number I was thinking of was ' + number)
    #if the above condition returns True, the a the string in the bracets will be displayed, including the variable
