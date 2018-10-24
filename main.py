userInput = input('Please enter a number: ')

for iterator in range((len(userInput) - 1), -1, -1):
    # print((10**iterator) * userInput[iterator])
    print(int(userInput[iterator]) * (10**iterator))