import numpy as np

l4 = [
    [
        [
            [10, 20],
            [30, 40]
        ],
        [
            [11, 21],
            [31, 41]
        ]
    ],
    [
        [[50, 60],
        [70, 80]
        ],
        [
            [51, 61],
            [71, 81]
        ]
    ]
]


arr4 = np.array(l4)
print(arr4[0:1, 1:2, 1:2, 0:1 ])
# print(arr4.shape)
# print(arr4.ndim)

# print(arr4[0,0,0,0])
# print(arr4[0,0,0,1])
# print(arr4[0,0,1,0])
# print(arr4[0,0,1,1])
# print(arr4[0,1,0,0])
# print(arr4[0,1,0,1])
# print(arr4[0,1,1,0])
# print(arr4[0,1,1,1])

# print(arr4[1,0,0,0])
# print(arr4[1,0,0,1])
# print(arr4[1,0,1,0])
# print(arr4[1,0,1,1])
# print(arr4[1,1,0,0])
# print(arr4[1,1,0,1])
# print(arr4[1,1,1,0])
# print(arr4[1,1,1,1]) 

#  for 4D arry [ block , row , col, chanel ]
#  for 3D arry [ block , col, chanel ]
#  for 2D arry [ block , chanel ]


# using slice method

# print("**********************. using slice method. **********************")

# print(arr4[0:2, 0:2, 0:2, 0:1 ].ndim)
# print(arr4[0:2, 0:2, 0:2, 0:1 ].shape)
# print(arr4[0:2, 0:2, 0:2, 0:1 ].size)



# print("**********************. fetch using for loop method. **********************")
# for i in arr4:
#     for j in i:
#         for k in j:
#             for l in k:
#                 print(l)



print("************************. fetch using shape method. ************************")
for i in range(arr4.shape[0]):
    for j in range(arr4.shape[1]):
       for k in range(arr4.shape[2]):
           for l in range(arr4.shape[2]):
            print(arr4[i,j,k,l])
print(arr4.shape)
