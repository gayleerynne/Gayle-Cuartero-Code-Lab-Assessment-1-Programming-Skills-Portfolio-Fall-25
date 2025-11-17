# defining the correct password
password = "12345" 

# adding number of attempts (Optional Requirements)
attempts = 5 

print ("Hello user. You have 5 attempts.")

# creating a while loop to repeatedly ask the user until the correct password is given
while True:
    password_attempt = str(input("Please input your password: "))
    
    if password_attempt == password: # when input matches the password, the following is printed
        print ("Access Granted. Welcome back")
        break # insert break to end the loop
    elif attempts == 1: # when attempts reaches 0, the following is printed and the program ends
        print ("Maximum number of attempts reached. Authorities have been alerted.")
        break # insert break to end the loop
    else: 
        attempts = attempts - 1 # after every wrong attempt, the counter goes down once
        print (f'Incorrect. You have {attempts} attempt(s) left. Please try again.')