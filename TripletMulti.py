# A easy funtion to calculate the product of the 3 highest number in a list og 3 or more elements

def maxProduct(array):

    n = len(array)
    
    # a check method which return -1 if the array is too small
    if n < 3: 
        return -1

    # The product of the highest triplet
    max_product = array[-1]*array[-2]*array[-3]

    return max_product


# Given a list
arr = [1, 10, 2, 6, 5, 3]

# Sorting the list from low to high
sorted = arr.sort()
 
# Calling our function
max = maxProduct(arr)
 

if max == -1:
    print("No Triplet Exits")
else:
    print("Maximum product is", max)