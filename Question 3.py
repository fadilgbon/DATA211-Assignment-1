#Question 3: Safe Function Application

pairs_of_numbers = [[12, 2], [4, -3], [6, 10], [5, 0]]

def compute_power_of_number(base_number,exponent_number): #funcyions taking parameters of pair (x,y)
    if exponent_number >= 0: #checks if exponent is negative
        return base_number**exponent_number #returns product
    else:
        return None #otherwise returns nothing

list_of_power_products = []
for pair in pairs_of_numbers: #loops through list of pairs
    power_product = compute_power_of_number(pair[0], pair[1]) #passes the x and y values of the pair list to the function as arguments
    if power_product is not None: #checks if the function returned a number
        list_of_power_products.append(power_product) #appends the number to the list of products
print(list_of_power_products)