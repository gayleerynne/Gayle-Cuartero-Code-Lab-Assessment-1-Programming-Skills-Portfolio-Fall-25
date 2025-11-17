#introduction and asking for the capital of france
print ("Hello there! I have a question for you!")
answer = input("What is the capital of France? ")

if answer.lower() == "PARIS".lower(): # .lower() makes the input correct regardless of capitalization
    print ("Wow you are correct!") # if the answer is correct, this is printed
else:
    print ("Not quite! The answer was Paris!") # if the answer is incorrect, this is printed

### Advanced Requirements

# extending the program to ask for 10 more capitals
print ("Now let's check your knowledge on the capitals of 10 european countries!") 

# creating a key dictionary with 10 european countries and their capitals
european_countries = {
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Russia": "Moscow",
    "Slovakia": "Bratislava",
    "Spain": "Madrid",
    "United Kingdom": "London"
}

# adding a score counter to see how many they get right out of 10
score = 0 

# creates a for loop for each country in the dictionary
for country, capital in european_countries.items(): # runs for each item in the dictionary
    answers = input(f'What is the capital of {country}? ')
    if answers.lower().strip() == capital.lower(): # disregards capitalization and addition of spaces
        print ("You are correct!")
        score = score + 1 # adds to the score counter every time they are right
    else:
        print (f'Wrong, the capital of {country} is {capital}.')


# ending the program, and displaying their score
print (f'Thanks for answering the questions! Your score is {score} out of 10.')
if score > 7:
    print ("You know a lot about countries and their capitals!") # when the score is 8 and above this is shown
else:
    print ("We are learning everyday!") # when the score is 7 and below, this is shown