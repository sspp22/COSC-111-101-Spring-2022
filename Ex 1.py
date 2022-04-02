print("Instructions: In a given list the last element should become the first one. An empty list or list with only one element should stay the same.")
def replace_last(array):
    new_array=[]
    for x,i in enumerate(array):
        n=(x+len(array)-1)%(len(array))
        new_array.append(array[n])
    new_array
    return (new_array)

print(replace_last([1, 2, 3, 4]))

def replace_last(array):
    new_array = array[-1:] + array[:-1]
    return new_array

print(replace_last([2, 3, 4, 1]))
