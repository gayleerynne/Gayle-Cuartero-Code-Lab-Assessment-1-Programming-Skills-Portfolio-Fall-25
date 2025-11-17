
# creating a list initialized with specific names
People = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# searching "Sam" directly in the list
if "Sam" in People:
    print ("Sam was found on the list!") 
else:
    print ("Sam is not in the list.")

### Optional Requirements

# asking the user to input the search term
person = input("Hello, enter the name of the person you wish to check on the list: ")

# if else statement to check if the inputted name is in the list
if person.strip().capitalize() in People:
    print (f'{person} was found on the list!')
else:
    print (f'{person} is not on the list.')