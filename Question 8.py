import pandas as pd

#Question 8: Pandas Dataframe with Computed Column
data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
 } #initalizes dictionary with 3 keys and list of numbers as its values

dataframe =pd.DataFrame(data) #changed the dictionary to a dataframe
dataframe["D"] = dataframe["B"]*dataframe["C"] #creates a new column in the dataframe "D" and gets its value by multiplying the value from column "B" and "C"
print(dataframe)