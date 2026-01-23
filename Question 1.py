#Question 1: Controlled Multiplication Loop
threshold = 250
product = 1
currentNumber = 1
while product < threshold: #it continues the loop until the product value exceeds the given threshold
    product *= currentNumber #multiplies the product variable by the given number
    currentNumber += 1 #increments current number to track the number being multiplied

print(f'The final product is {product} and the integer that caused this is  {currentNumber}')