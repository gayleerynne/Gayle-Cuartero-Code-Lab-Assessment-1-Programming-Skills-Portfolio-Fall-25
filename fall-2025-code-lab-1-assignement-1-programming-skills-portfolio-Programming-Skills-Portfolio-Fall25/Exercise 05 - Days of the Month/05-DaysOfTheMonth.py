# creating a dictionary with months as keys and the number of days as values
months_days = {
    1: "31",
    2: "28",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31",
}

# giving values to the months
month_names = {
1: "January",
2: "February",
3: "March",
4: "April",
5: "May",
6: "June",
7: "July",
8: "August",
9: "September",
10: "October",
11: "November",
12: "December",
}

# introduction and input handling
print ("Hello there! I am here to tell you the number of days in any month you wish!")

### Advanced Requirements

# checking if it is a leap year
while True: # using a while loop to keep on asking until user inputs a valid answer
    leap_year = str(input("Is the year you want to check a leap year? (yes/no) "))
    if leap_year.strip().lower() == "yes":
        months_days[2] = "29" # changes the value of february from 28 to 29
        break
    elif leap_year.strip().lower() == "no": # changes nothing to the original dictionary
        break
    else:
        print ("Invalid output. Please enter yes or no.")


# ensuring it is a valid number
while True: # creates a loop until the user enters a valid number
        month_input = int(input("Please input the number that corresponds to the month you wish to check (e.g., 1: January): "))
        
        if month_input <= 12 and month_input >= 1:
            month_name = month_names[month_input]
            days = months_days[month_input]
            print (f'There are {days} days in the month of {month_name}.')
            print ("Thanks for using the month checker!")
            break # stops the loop when valid number is entered
        else:
            print ("Invalid month, please try numbers from 1-12")
    