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
print(arr4.shape)
print(arr4.ndim)

print(arr4[0,0,0,0])
print(arr4[0,0,0,1])
print(arr4[0,0,1,0])
print(arr4[0,0,1,1])
print(arr4[0,1,0,0])
print(arr4[0,1,0,1])
print(arr4[0,1,1,0])
print(arr4[0,1,1,1])

print(arr4[1,0,0,0])
print(arr4[1,0,0,1])
print(arr4[1,0,1,0])
print(arr4[1,0,1,1])
print(arr4[1,1,0,0])
print(arr4[1,1,0,1])
print(arr4[1,1,1,0])
print(arr4[1,1,1,1])