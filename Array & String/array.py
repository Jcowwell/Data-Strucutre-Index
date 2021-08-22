# Header

# helper variables
size = 10
width = 10
height = 10

# intialize a sinlge-dimensional "array"
array = [0] * size

# creates a two-dimensional array with "height" # of refernces to the list made from [[0] * width]
array = [[0] * width] * height
# sets 1 to the [0][0]th position of th list but will affect all [0][i] positions since this two-dimnensional array is just height # of references. 
array[0][0] = 1
# 0: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 2: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 3: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 4: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 5: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 6: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 7: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 8: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 9: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# uses list comprehension to ensure that each row is a newly generated "array"
array = [[0 for _ in range(width)] for _ in range(height)]
array[0][0] = 1
# 0: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 7: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 8: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
