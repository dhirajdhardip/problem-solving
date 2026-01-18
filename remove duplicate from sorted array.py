

nums = int(input("How many number do you want: "))
array = []

print("Enter the number of array element: ")
for _ in range(nums):
    array.append(int(input()))

array.sort()

def removeDuplicate(array):
  
    i = 0  
    for j in range(1, len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
          
    return i + 1  
unique_count = removeDuplicate(array)

print("Unique element count: ", unique_count)
print("Array without duplicates: ", array[:unique_count])
