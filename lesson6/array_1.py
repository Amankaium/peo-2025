my_array = [6, 7, 0, "hello", False, None]
# print(my_array)

array_2 = [
    [7, 3, 9, 5],
    [4,	5, 0, 7],
    [1,	6, 2, 3],
]

# for i in range(3):
#     print(array_2[i])

# for f in array_2: # [7, 3, 9, 5]
#     # f - это список
#     for n in f: # 7 # 3
#         print(n)
a = int(input("google: "))
for i in range(3): # 0
    # array_2[i] - список
    for j in range(4): # 0
        if array_2[i][j] == a:
            print(i, j, array_2[i][j])
        
# print(array_2[0][2])
# print(array_2[0][1])
# print(array_2[2][3])
