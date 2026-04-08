#matrix functions in numpy
import numpy as np

l1=[[2,3],
    [6,7]],
    # [1,4]
l2=[[1,4],
    [5,8]]
ar1=np.array(l1)
ar2=np.array(l2)

# res=ar1*ar2
# print(res)

# res1=np.matmul(ar1,ar2)
# res3=np.dot(ar1,ar2)
# res2=ar1@ar2
# print(res1)
# print(res3)
# print(res2)

#inverse of a matrix
# inv_mt=np.linalg.inv(ar1)
# print(inv_mt)

#determinant of a matrix
# det=np.linalg.det(ar1)
# print(det)

#singular value decomposition
# u,s,v=np.linalg.svd(ar1)
# print("U matrix:")
# print(u)
# print("Singular values:")
# print(s)
# print("V matrix:")
# print(v)

#eigenvalues and eigenvectors
# eigenvalues,eigenvectors=np.linalg.eig(ar1)
# print("Eigenvalues:")
# print(eigenvalues)
# print("Eigenvectors:")
# print(eigenvectors)

#trace of a matrix
# trace=np.trace(ar1)
# print("Trace of the matrix:")
# print(trace)

# #transpose of a matrix
# transpose=np.transpose(ar1)
# print("Transpose of the matrix:")
# print(transpose)

# #eye matrix
# eye_matrix=np.eye(3)
# print("Eye matrix:")
# print(eye_matrix)   

# #rank of a matrix
# rank=np.linalg.matrix_rank(ar1)
# print("Rank of the matrix:")
# print(rank)

#solve linear equations
# a=np.array([[3,2],[1,4]])
# b=np.array([5,6])
# solution=np.linalg.solve(a,b)
# print("Solution of the linear equations:")
# print(solution)