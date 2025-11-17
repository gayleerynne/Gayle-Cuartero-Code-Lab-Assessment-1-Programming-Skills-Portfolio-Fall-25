# storing information in variables
my_name = "Gayle"
my_hometown = "Philippines"
my_age = "17"

# storing the information as key-value pairs in a dictionary
myself = {
    "my_name": "Gayle",
    "my_hometown": "Philippines",
    "my_age": "17"
}

# introducing myself 
print (f'Hi there! my name is {my_name}.', f'I am from the {my_hometown}', f'and I am {my_age} years old.','what about you?', sep="\n")  #used sep="\n" to separate information per line

### Advanced Requirements

# having the user input their own name, hometown, and age
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Preventing the issue if user types age using string value
while True:
    age = int(input("Enter your age: "))
    if age > 0 and age <100:
        break
    else:
        print("Please enter a valid number for your age! (e.g.: 18)")

# store user's information as key-value pairs in a dictionary
user_info = {
    "name":name,
    "hometown": hometown,
    "age": age
}

# printing the user's information on separate lines using a single print statement
print(
    f'Hi there {name}!', f'I see that you are from {hometown}, nice place!', f'And you are {age} years old!, It is nice to meet you!', sep="\n") #used sep="\n" to separate information per line