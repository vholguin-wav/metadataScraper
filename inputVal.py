# Basic input validation script
# Vincent Holguin - Dec 2024

# Check that input is an int
def inputInt(message_in = ''):                  #Optional message like a regular input
    while True:                                 #Loop works to perform check
        try:
            val = int(input(message_in))        #Convert input to an int
            return val                          #Return val
        except ValueError:
            print('Please enter a valid int.')  #Error message, will continue loop

# Check that input is a float, if it is an int conv to float and return
def inputFloat(message_in=''):
    while True:
        try:
            val = float(input(message_in))      # Convert input to a float
            return val                          # Return val
        except ValueError:
            print('Please enter a valid float.')

# Because input already returns a str, this verifies the str is not empty
def inputStr(message_in = ''):
    while True:
        val = input(message_in)                 # Assign val the input str
        if val.strip():                         # True if not empty
            return val
        else:                                   # If str in empty continue until valid input
            print('Please enter a valid, non-empty str.')



# intTest = inputInt('Enter an integer: ')
# print(f'You entered {intTest} and the data is type: {type(intTest)}')
# floatTest = inputFloat('Enter a float: ')
# print(f'You entered {floatTest} and the data is type: {type(floatTest)}')
# strTest = inputStr('Enter a str: ')
# print(f'You entered {strTest} and the data is type: {type(strTest)}')

