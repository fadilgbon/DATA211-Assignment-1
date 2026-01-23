import random
#Question 4: Sorted Search with Conditions

list_of_random_values =[random.random() for i in range(10)] #creates a list of  10 random values from 0 to 1
random_value = random.random() # creates a random value to compare to the list
sorted_list_of_random_values = sorted(list_of_random_values) #sorts the list of random values from list to greatest
indices_where_list_value_is_greater_than_random_value = [] #initilaization of the dictionary of all indices where the list value is greater than the random value
for value in sorted_list_of_random_values: #loops through the sorted list
    if value >= random_value: #checks if the value in the list if greater than or equal to the random number
        indices_where_list_value_is_greater_than_random_value.append(random_value)#appends the number to the list

print(f"Sorted values: {sorted_list_of_random_values}")
print(f"Random Comparison Value: {random_value} ")

if indices_where_list_value_is_greater_than_random_value: #checks if the list of indices is empty
    print(f"First index where list value is Greater Than or Equal to the Random Comparison Value:{indices_where_list_value_is_greater_than_random_value[0]}")
else:
    print("No value in the list are greater than or equal to Random Comparison Value")

