
# function that determines if the value is even or odd
def odd_even_checker(number):
    if number % 2 == 0: # uses % to find the remainder of the number when divided by 2
        return (f'The number {number} is even.')
    else:
        return (f'The number {number} is odd.')

# main function asks the user for a number
def main():
    number_input = int(input("Please input a number: "))
    result = odd_even_checker(number_input)
    print (result) # the message returned is printed within the main function

main() # calling the main() function