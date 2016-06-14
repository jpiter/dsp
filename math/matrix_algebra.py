# Matrix Algebra
import numpy as np

# Part 1
print("\nPart 1:\n")

A = np.array([[1,2,3],[2,7,4]])
print("\nA = ")
print(A)
print("dim A = ", A.shape)

B = np.array([[1,-1],[0,1]])
print("\nB = ")
print(B)
print("dim B = ", B.shape)

C =np.array([[5,-1],[9,1],[6,0]])
print("\nC =")
print(C)
print("dim C = ", C.shape)

D = np.array([[3,-2,-1],[1,2,3]])
print("\nD =")
print(D)
print("dim D = ", D.shape)

u =  np.array([[6,2,-3,5]])
print("\nu = ", u)
print("dim u = ", u.shape)

v = np.array([[3,5,-1,4]])
print("\nv = ", v)

w = np.array([[1],[8],[0],[5]])
print("\nw = ")
print(w)
print("dim w = ", w.shape)

#Part 2
print("\nPart 2:\n")

print("\nu + v = ", u + v)

print("\nu - v = ", u - v)

alpha = 6
print("\nalpha * v = ", alpha * v)

print("\n<u,v> = ", np.vdot(u,v))

print("\n||u|| = ", np.linalg.norm(u))

#Part 3
print("\nPart 3:")

print("\nA - C is not defined!")

print("\nA - C^t = ")
print(A - C.T)

print("\nC^t + 3D = ")
print(C.T + 3 * D)

print("\nBA = ")
print(np.dot(B,A))

print("\nBA^t is not defined!")

#Part 3
print("\nOptional:\n")

print("\nBC is not defined!")

print("\nCB = ")
print(np.dot(C,B))

print("\nB^4 = ")
print(np.linalg.matrix_power(B, 4))

print("\nAA^t = ")
print(np.dot(A,A.T))

print("\nD^tD = ")
print(np.dot(D.T,D))

