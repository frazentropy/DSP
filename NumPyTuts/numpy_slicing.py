import numpy as np
a = np.arange(10)
s = slice(2,7,2)
print(a[s])

b = a[2:7:2]
print(b)

b = a[5]
print(b)

# slice items starting from index
print(a[2:])

# slice items between indices
print(a[2:5])

# slice items starting from index
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print('Now we will slice the array from the index a[1:]')
print(a[1:])

print('Our array is:')
print(a)
print('\n')

# this returns array of items in the selected column
print('The items in the second column are:')
print(a[...,1])
print('\n')

# now we will slice all items from the second row
print('The items in the second row are:')
print(a[1,...])
print('\n')

# now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[...,1:])
