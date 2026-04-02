array = input("list:").split(",") #takes a list of numbers as input and seperates them by commas
offset = float(input("offset:")) #takes a number as input as sets it as the offset
val = 0 #sets the val variable to 0
for i in array: #iterates through the array and adds each number together
    i = float(i)
    val += i

mean = val / len(array) #divides the total val by the length of the array to get the mean
new_mean = mean + offset #adds the offset to the mean to get a new mean
print(new_mean) #prints the new mean