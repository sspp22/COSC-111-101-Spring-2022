print("You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.")
def index_power(array,index):
    try:
        array[index]    
    except IndexError:
        x=-1
        return x
    x=array[index]**index
    return x
print(index_power([1, 2, 3, 4], 2))
