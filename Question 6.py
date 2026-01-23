import random
#Question 6: Distribution Analysis

list_of_numbers = [random.randint(1,10) for i in range(7)] #intializes

def frequency_of_numbers_in_a_list(list_of_numbers): #intializes dunction
    dictionary_of_numbers = {} #intializes empty dictionary
    for number in list_of_numbers: #loops through the numbers in the list
        if number not in dictionary_of_numbers: #checks if the number exists in as a key in the list
            dictionary_of_numbers[number] = 1 #if the number isn't in the dictionary it adds it and ste sits value to 1
        else:
            dictionary_of_numbers[number] += 1 #else it adds 1 ot the value of the key in the list
    return dictionary_of_numbers #returns the dictionar

numbers_dictionary = frequency_of_numbers_in_a_list(list_of_numbers)
print(list_of_numbers)
print(numbers_dictionary)