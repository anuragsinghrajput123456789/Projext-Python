from time import time
import random as r

print(time())

# Function to calculate mistakes
def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        if i >= len(usertest) or partest[i] != usertest[i]:
            error += 1
    return error

# Function to calculate typing speed
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    if time_R > 0:  # To avoid division by zero
        speed = len(userinput) / time_R
        return round(speed, 2)
    return 0

# Main function
if __name__ == '__main__':
    while True:
        ck = input("Ready to test? (yes/no): ").lower()
        if ck == "yes":
            test = [
                "A paragraph is a self-contained unit of discourse in writing, dealing with a particular point or idea.",
                "My name is Vishal.",
                "Welcome to YMCA!"
            ]
            test1 = r.choice(test)
            print("***** Typing Speed *****")
            print(test1)
            print()
            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()

            print('Speed: ', speed_time(time_1, time_2, testinput), "w/sec")
            print("Error: ", mistake(test1, testinput))

        elif ck == 'no':
            print("Thank you!")
            break
        else:
            print("Wrong input, please type 'yes' or 'no'.")
