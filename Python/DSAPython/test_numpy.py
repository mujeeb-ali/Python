import numpy as np
# # print(np.__version__)
# # x = np.random.rand(5)
# # print(x)

# # y = np.random.rand(3,3)
# # print(y)

# import numpy as np

# x = np.random.randint(1, 10, (5, 5))
# filter = x[x % 2 == 1]   # take odd elements

# print("Filtered:", filter)
# print("Count:", filter.size)

# # reshape only if possible
# if filter.size == 16:
#     reshapefilter = filter.reshape(4, 4)
#     print(reshapefilter)
# else:
#     print("Cannot reshape to (4,4), size mismatch")

x = np.random.randint(1, 10, (5, 5))
filter = x[x > 7]  

filter = x[x%2 == 1]   # take odd elements

x = np.array([[2,30,20,-2,-4],[1,3,5,7,9],[10,20,30,40,50],[11,13,15,17,19],[6,8,4,2,0]])
x[x<0] = 0
x[x%2 == 1] = -2
print(x)