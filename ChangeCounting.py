p = int(input("Enter number of pennies: ")) #declares p as the the number of pennies via user input
n = int(input("Enter number of nickels: ")) #declares n as the the number of nickels via user input
d = int(input("Enter number of dimes: ")) #declares d as the the number of dimes via user input
q = int(input("Enter number of quarters: ")) #declares q as the the number of quarters via user input

sum = float((.01 * p) + (.05 * n) + (.1 * d) + (.25 * q)) #calculates the sum of the inputs based on the monetary value of each input

if sum == 1:
    print("Congratulations, you win the game!") #user wins the game if the sum equals 1 dollar
elif sum < 1:
    difference = (1 - sum);
    print("You are " + str(difference) + " away from 1 dollar") #calculates the difference between the sum and 1 dollar if the sum > 1
else:
    difference = (sum - 1);
    print("You are " + str(difference) + " away from 1 dollar") #calculates the difference between the sum and 1 dollar if the sum < 1